import argparse
import difflib
from core.models import Profile
from core.registry import TOOL_METADATA, SYSTEM_OS
from services.profile import ProfileService
from services.installer import InstallationService
from ui.view import console, CLIView
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
from rich.prompt import Confirm

VERSION = "1.0.0"
ALL_TOOLS = list(TOOL_METADATA.get(SYSTEM_OS, {}).keys())


def validate_tool(tool: str) -> bool:
    """Validates if a tool exists in the registry and suggests alternatives."""
    if tool not in ALL_TOOLS:
        matches = difflib.get_close_matches(tool, ALL_TOOLS, n=3, cutoff=0.5)
        CLIView.render_error_suggestion(tool, matches)
        return False
    return True


def execute_scan_with_loader(profile: Profile, description: str = "Scanning"):
    """Wraps the blocking system scan in a transient loader."""
    with Progress(
        SpinnerColumn("dots", style="info"),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task(description, total=len(profile.tools))

        def update_progress(tool_name, idx, total):
            progress.update(
                task, description=f"Scanning [info]{tool_name}[/info]...", advance=1
            )

        return ProfileService.scan_profile(profile, progress_callback=update_progress)


def handle_scan(args):
    CLIView.render_header(f"DevSetup v{VERSION}")
    profile_name = getattr(args, "profile", None)

    if profile_name:
        try:
            profile = ProfileService.load(profile_name)
            installed, missing = execute_scan_with_loader(profile)

            score = (
                (len(installed) / len(profile.tools) * 100) if profile.tools else 100.0
            )

            CLIView.render_profile_analysis(
                profile.name,
                len(profile.tools),
                len(installed),
                len(missing),
                score,
                missing,
            )
        except FileNotFoundError:
            console.print(f"[error]Error: Profile '{profile_name}' not found.[/error]")
        return

    # Global Scan
    target = Profile(name="global", description="System Discovery", tools=ALL_TOOLS)
    installed, missing = execute_scan_with_loader(
        target, description="Discovering system tools"
    )

    CLIView.render_scan_report(installed, missing)
    health = (
        (len(installed) / (len(installed) + len(missing)) * 100) if installed else 0
    )
    CLIView.render_summary(len(installed), len(missing), health)


def execute_install_sequence(profile: Profile):
    installed, missing = execute_scan_with_loader(
        profile, description="Verifying current state"
    )

    plan = []
    for t in installed:
        plan.append({"tool": t.name, "version": t.version, "action": "Skip"})
    for t in missing:
        plan.append({"tool": t, "version": "latest", "action": "Install"})
    CLIView.render_install_plan(plan)

    if not missing:
        console.print("[success]✓ Everything is already up to date.[/success]")
        return

    if not Confirm.ask("Proceed with installation?", default=True, console=console):
        return

    console.print("\nInstalling Tools", style="bold white")
    results = []

    for idx, tool in enumerate(missing, 1):
        console.print(f"[{idx}/{len(missing)}] Installing {tool.capitalize()}...")

        with Progress(
            SpinnerColumn("dots"),
            TextColumn("Downloading..."),
            BarColumn(bar_width=30, complete_style="cyan", finished_style="cyan"),
            TextColumn("{task.percentage:>3.0f}%"),
            console=console,
            transient=True,
        ) as progress:
            task = progress.add_task("", total=100)

            version = (
                next(
                    (t["version"] for t in profile.frozen_tools if t["name"] == tool),
                    None,
                )
                if profile.is_freezed
                else None
            )

            success, error_msg = InstallationService.install(tool, version)
            progress.update(task, completed=100)

        if success:
            console.print("[success]✓ Completed[/success]\n")
        else:
            console.print("[error]✗ Failed[/error]\n")

        results.append({"tool": tool, "success": success, "error": error_msg})

    CLIView.render_install_results(results)


def handle_install(args):
    CLIView.render_header(f"DevSetup v{VERSION}")
    try:
        execute_install_sequence(ProfileService.load(args.profile))
    except FileNotFoundError:
        console.print(f"[error]Error: Profile '{args.profile}' not found.[/error]")


def handle_install_tool(args):
    CLIView.render_header(f"DevSetup v{VERSION}")
    if not validate_tool(args.tool):
        return

    console.print(f"Installing {args.tool}...")
    with console.status(f"[info]Installing {args.tool}...[/info]"):
        success, error_msg = InstallationService.install(args.tool)

    if success:
        CLIView.render_success(f"{args.tool} Installed Successfully", [])
    else:
        console.print(f"\n[error]✗ Failed to install {args.tool}[/error]")
        if error_msg:
            console.print(
                f"  [secondary]Reason: {error_msg.splitlines()[0]}[/secondary]\n"
            )


def handle_init(args):
    CLIView.render_header(f"DevSetup v{VERSION}")

    try:
        tools_input = input(
            "Enter required tools for this project (comma separated): "
        ).strip()
        tools = [t.strip() for t in tools_input.split(",") if t.strip()]

        for t in tools:
            if not validate_tool(t):
                return

        name = (
            input("Project Name (default: local-project): ").strip() or "local-project"
        )
        ProfileService.save_local(
            Profile(name=name, description="Local environment", tools=tools)
        )
        CLIView.render_success(
            "Project Initialized", ["Name     : " + name, "File     : .devsetup.json"]
        )
    except KeyboardInterrupt:
        console.print("\n[secondary]Initialization cancelled.[/secondary]")


def handle_profile(args):
    """Router for profile subcommands."""
    if args.profile_command == "list":
        CLIView.render_header(f"DevSetup v{VERSION}")
        profiles = ProfileService.list_all()
        CLIView.render_profile_list(profiles)

    elif args.profile_command == "show":
        CLIView.render_header(f"DevSetup v{VERSION}")
        try:
            profile = ProfileService.load(args.name)
            CLIView.render_profile_details(profile)
        except FileNotFoundError:
            console.print(f"[error]Error: Profile '{args.name}' not found.[/error]")

    elif args.profile_command == "export":
        CLIView.render_header(f"DevSetup v{VERSION}")
        try:
            path = ProfileService.export_profile(args.name, freeze=args.freeze)
            CLIView.render_success(
                "Profile Exported", [f"Name     : {args.name}", f"Location : {path}"]
            )
        except FileNotFoundError:
            console.print(f"[error]Error: Profile '{args.name}' not found.[/error]")

    elif args.profile_command == "import":
        CLIView.render_header(f"DevSetup v{VERSION}")
        try:
            name = ProfileService.import_profile(args.filepath)
            CLIView.render_success(
                "Profile Imported",
                [f"Name     : {name}", f"Source   : {args.filepath}"],
            )
        except FileNotFoundError:
            console.print(f"[error]Error: File '{args.filepath}' not found.[/error]")
        except Exception as e:
            console.print(f"[error]Failed to import profile: {e}[/error]")
    else:
        # If the user just types `devsetup profile` with no subcommand
        console.print(
            "[error]Missing profile command. Use: list, show, export, or import[/error]"
        )


def handle_sync(args):
    CLIView.render_header(f"DevSetup v{VERSION}")
    try:
        execute_install_sequence(ProfileService.load_local())
    except FileNotFoundError as e:
        console.print(f"[error]Error:[/error] {e}")


def handle_report(args):
    CLIView.render_header(f"DevSetup v{VERSION}")
    installed, missing = execute_scan_with_loader(
        Profile(name="global", description="", tools=ALL_TOOLS),
        description="Generating system report",
    )
    CLIView.render_system_report(installed, missing)


def main():
    parser = argparse.ArgumentParser(description="DevSetup Tool")
    subparsers = parser.add_subparsers(dest="command")

    # --- Restore Missing Top-Level Commands ---
    scan_p = subparsers.add_parser("scan", help="Scan system or a specific profile")
    scan_p.add_argument("profile", nargs="?", help="Target profile name")

    inst_p = subparsers.add_parser("install", help="Install tools from a profile")
    inst_p.add_argument("profile", help="Target profile name")

    inst_tool_p = subparsers.add_parser("install-tool", help="Install a specific tool")
    inst_tool_p.add_argument("tool", help="Name of the tool")

    subparsers.add_parser("init", help="Initialize a local project profile")
    subparsers.add_parser("sync", help="Sync tools from the local .devsetup.json profile")
    subparsers.add_parser("report", help="Generate a comprehensive system report")
    subparsers.add_parser("version", help="Show CLI version")
    # ------------------------------------------

    # --- Profile Command Group ---
    profile_p = subparsers.add_parser("profile", help="Manage DevSetup profiles")
    profile_subs = profile_p.add_subparsers(dest="profile_command")

    profile_subs.add_parser("list", help="List all available profiles")

    show_p = profile_subs.add_parser("show", help="Show details of a profile")
    show_p.add_argument("name", help="The name of the profile to inspect")

    export_p = profile_subs.add_parser("export", help="Export a profile to a JSON file")
    export_p.add_argument("name", help="The name of the profile to export")
    export_p.add_argument(
        "--freeze",
        action="store_true",
        help="Lock the tool versions to currently installed versions",
    )

    import_p = profile_subs.add_parser("import", help="Import a profile from a JSON file")
    import_p.add_argument("filepath", help="Path to the JSON profile file")
    # ----------------------------------

    args = parser.parse_args()

    # Route commands
    if args.command == "scan":
        handle_scan(args)
    elif args.command == "report":
        handle_report(args)
    elif args.command == "install":
        handle_install(args)
    elif args.command == "install-tool":
        handle_install_tool(args)
    elif args.command == "init":
        handle_init(args)
    elif args.command == "sync":
        handle_sync(args)
    elif args.command == "version":
        CLIView.render_header(f"DevSetup v{VERSION}")
    elif args.command == "profile": 
        handle_profile(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()