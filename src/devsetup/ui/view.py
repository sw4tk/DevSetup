from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box
import platform
from ui.styles import APP_THEME, Icons, MINIMAL_TABLE
from core.models import ToolStatus
from core.registry import TOOL_CATEGORIES
from typing import List, Dict

# highlight=False prevents Rich from randomly syntax-highlighting text (like versions)
console = Console(theme=APP_THEME, highlight=False)


class CLIView:

    @staticmethod
    def render_profile_details(profile):
        CLIView.render_header(f"Profile: {profile.name}")
        console.print(
            f"  [secondary]Description :[/secondary] {profile.description or 'No description provided.'}"
        )
        console.print(
            f"  [secondary]Created     :[/secondary] {profile.date_created or 'Unknown'}"
        )

        status_tag = (
            f"{Icons.LOCK} [warning]Frozen[/warning]"
            if profile.is_freezed
            else f"{Icons.INFO} [info]Dynamic[/info]"
        )
        console.print(f"  [secondary]Status      :[/secondary] {status_tag}")
        console.print()

        table = Table(box=MINIMAL_TABLE, expand=False, collapse_padding=True)
        table.add_column("Tools Included", style="header", min_width=20)
        table.add_column("Version Constraint", style="secondary")

        if not profile.tools:
            console.print(
                "  [secondary]No tools configured in this profile.[/secondary]\n"
            )
            return

        if profile.is_freezed:
            for t in profile.frozen_tools:
                table.add_row(f"{Icons.BULLET} {t['name']}", t["version"] or "latest")
        else:
            for t in profile.tools:
                table.add_row(f"{Icons.BULLET} {t}", "latest")

        console.print(table)
        console.print()


    @staticmethod
    def render_header(text: str = "DevSetup"):
        console.print()
        console.print(f"  {text}", style="header")
        console.print()

    @staticmethod
    def render_scan_report(installed: List[ToolStatus], missing: List[str]):
        CLIView.render_header("Scanning local environment...")

        table = Table(box=MINIMAL_TABLE, expand=False, collapse_padding=True)
        table.add_column("Tool", style="header", min_width=15)
        table.add_column("Version", style="secondary", min_width=10)
        table.add_column("Status", min_width=15)
        table.add_column("Category", style="secondary")

        # Add installed tools
        for item in installed:
            cat = TOOL_CATEGORIES.get(item.name, "Uncategorized")
            table.add_row(
                item.name,
                item.version or "-",
                f"{Icons.SUCCESS} Installed",
                f"{Icons.BULLET} {cat}",
            )

        # Add missing tools
        for item in missing:
            cat = TOOL_CATEGORIES.get(item, "Uncategorized")
            table.add_row(item, "-", f"{Icons.ERROR} Missing", f"{Icons.BULLET} {cat}")

        console.print(table)
        console.print()

    @staticmethod
    def render_summary(installed_count: int, missing_count: int, health: float):
        if health >= 95:
            status = f"{Icons.SUCCESS} Excellent"
        elif health >= 80:
            status = f"{Icons.SUCCESS} Good"
        elif health >= 60:
            status = f"{Icons.WARNING} Fair"
        else:
            status = f"{Icons.ERROR} Needs Attention"

        rec = (
            "Environment is ready"
            if missing_count == 0
            else f"Run `devsetup install` to fix {missing_count} tools"
        )

        content = (
            f"\n"
            f"   Status      :  {status}\n"
            f"   Health      :  {health:.1f}% Match\n"
            f"   Missing     :  {missing_count} tools require installation\n"
            f"\n"
            f"   Next Step   :  {rec}\n"
        )

        console.print(
            Panel(
                content,
                title=" Environment Summary ",
                title_align="left",
                border_style="panel_border",
                box=box.ROUNDED,
                expand=False,
            )
        )
        console.print()

    @staticmethod
    def render_profile_analysis(
        name: str,
        required: int,
        installed: int,
        missing: int,
        score: float,
        missing_tools: List[str],
    ):
        CLIView.render_header(f"Profile Analysis: {name}")

        console.print("  Overview", style="header")
        console.print(f"  {Icons.BULLET} Match Score   :  {score:.1f}%")
        console.print(
            f"  {Icons.BULLET} Installed     :  {installed} of {required} required tools"
        )
        console.print(f"  {Icons.BULLET} Missing       :  {missing} tools\n")

        if missing > 0:
            table = Table(box=MINIMAL_TABLE, expand=False, collapse_padding=True)
            table.add_column("Missing Tool", style="header", min_width=15)
            table.add_column("Category", style="secondary")
            for t in missing_tools:
                table.add_row(
                    t, f"{Icons.BULLET} {TOOL_CATEGORIES.get(t, 'Uncategorized')}"
                )
            console.print(table)
            console.print()

    @staticmethod
    def render_install_plan(plan: List[Dict], is_frozen: bool = False):
        title = (
            f"{Icons.LOCK} Locked Profile Installation"
            if is_frozen
            else "Installation Plan"
        )
        CLIView.render_header(title)

        table = Table(box=MINIMAL_TABLE, expand=False, collapse_padding=True)
        table.add_column("Tool", style="header", min_width=15)
        table.add_column("Target Version", style="secondary", min_width=15)
        table.add_column("Action")

        to_install = 0
        to_skip = 0

        for p in plan:
            action_text = p["action"]
            if action_text.lower() == "install":
                to_install += 1
                display_action = f"{Icons.PLUS} Install"
            else:
                to_skip += 1
                display_action = f"{Icons.MINUS} Skip (Match)"

            table.add_row(p["tool"], p["version"] or "latest", display_action)

        console.print(table)
        console.print(
            f"\n  Plan: {to_install} to install, {to_skip} to skip.", style="secondary"
        )

        if is_frozen:
            console.print(
                f"\n  {Icons.WARNING} Notice: This is a frozen profile. Tools will be pinned"
            )
            console.print(
                "    to the exact versions specified in the lockfile.\n",
                style="secondary",
            )
        else:
            console.print()

    @staticmethod
    def render_install_results(results: List[Dict], time_elapsed: float = 0.0):
        content = "\n"
        success_count = 0

        for r in results:
            if r["success"]:
                content += f"   {Icons.SUCCESS}  {r['tool']} successfully installed\n"
                success_count += 1
            else:
                content += f"   {Icons.ERROR}  {r['tool']} failed to install\n"

                # Format and display the exact error reason
                if r.get("error"):
                    # Split by newline and take the first relevant line to prevent UI flooding
                    error_line = r["error"].split("\n")[0].strip()
                    # Truncate if it's absurdly long
                    if len(error_line) > 60:
                        error_line = error_line[:57] + "..."
                    content += f"      [secondary]Reason: {error_line}[/secondary]\n"

        content += f"\n   Time: {time_elapsed:.1f}s\n"

        console.print(
            Panel(
                content,
                title=" Installation Complete ",
                title_align="left",
                border_style="panel_border",
                box=box.ROUNDED,
                expand=False,
            )
        )
        console.print()

    @staticmethod
    def render_system_report(installed: List[ToolStatus], missing: List[str]):
        CLIView.render_header("System Environment Report")

        # Section 1: System Info
        console.print("  System Information", style="secondary")
        console.print(Rule(style="dim", align="left"))
        console.print(
            f"  OS Architecture :  {platform.system()} {platform.release()} ({platform.machine()})"
        )
        console.print(f"  Base Runtime    :  Python {platform.python_version()}\n")

        # Section 2: Health
        total_tools = len(installed) + len(missing)
        health = (len(installed) / total_tools * 100) if total_tools > 0 else 0

        console.print("  Health Dashboard", style="secondary")
        console.print(Rule(style="dim", align="left"))
        console.print(f"  Total Score     :  {health:.0f}%")
        console.print(f"  Tools Tracked   :  {total_tools} available in registry")
        console.print(f"  Installed       :  {len(installed)}")
        console.print(f"  Missing         :  {len(missing)}\n")

    @staticmethod
    def render_error_suggestion(tool: str, matches: list):
        console.print(f"\n  {Icons.ERROR} Unknown Tool: '{tool}'\n")
        console.print(
            f"  The tool '{tool}' is not registered in the DevSetup registry.\n",
            style="secondary",
        )

        if matches:
            console.print("  Did you mean:")
            for m in matches:
                console.print(f"  {Icons.BULLET} {m}")

        console.print(
            "\n  Run `devsetup registry list` to see all supported tools.\n",
            style="secondary",
        )

    @staticmethod
    def render_success(title: str, lines: List[str]):
        console.print(f"\n  {Icons.SUCCESS} {title}\n")
        for line in lines:
            console.print(f"  {Icons.BULLET} {line}")
        console.print()

    @staticmethod
    def render_profile_list(profiles: Dict[str, List[str]]):
        CLIView.render_header("Available Profiles")

        if not profiles:
            console.print(
                "  [secondary]No profiles found. Run `devsetup init` to create one.[/secondary]\n"
            )
            return

        for category, items in profiles.items():
            table = Table(box=MINIMAL_TABLE, expand=False, collapse_padding=True)
            table.add_column(category.capitalize(), style="header", min_width=25)
            table.add_column("Type", style="secondary")

            for item in items:
                table.add_row(item, f"{Icons.BULLET} Profile")

            console.print(table)
            console.print()
