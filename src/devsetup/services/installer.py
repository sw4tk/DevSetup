import subprocess
from typing import Optional, Tuple
from core.registry import SYSTEM_OS, TOOL_METADATA, DEPENDENCY_TOOLS
from services.executor import SystemExecutor


class InstallationService:
    @classmethod
    def install(cls, tool: str, version: Optional[str] = None) -> Tuple[bool, str]:
        # If dependency is met, return success and an empty string
        if tool in DEPENDENCY_TOOLS:
            parent = DEPENDENCY_TOOLS[tool]
            status, _ = SystemExecutor.check_tool_status(parent)
            if status:
                return True, ""

        native_package = TOOL_METADATA.get(SYSTEM_OS, {}).get(tool)
        if not native_package:
            return False, f"Tool '{tool}' not supported on {SYSTEM_OS}"

        try:
            if SYSTEM_OS == "windows":
                cmd = [
                    "winget",
                    "install",
                    "--id",
                    native_package,
                    "--exact",
                    "--accept-package-agreements",
                    "--accept-source-agreements",
                    "--silent",
                ]
                if version:
                    cmd.extend(["--version", version])
                res = subprocess.run(cmd, capture_output=True, text=True)
                if res.returncode == 0 or "already installed" in res.stdout.lower():
                    return True, ""
                return False, res.stderr.strip() or res.stdout.strip()

            elif SYSTEM_OS == "mac":
                cmd = ["brew", "install", native_package]
                res = subprocess.run(cmd, capture_output=True, text=True)
                if res.returncode == 0:
                    return True, ""
                return False, res.stderr.strip() or res.stdout.strip()

            elif SYSTEM_OS == "linux":
                cmd = ["sudo", "apt-get", "install", "-y", native_package]
                res = subprocess.run(cmd, capture_output=True, text=True)
                if res.returncode == 0:
                    return True, ""
                return False, res.stderr.strip() or res.stdout.strip()

        except FileNotFoundError as e:
            return False, f"Package manager not found: {e}"

        return False, "Unknown system or error occurred."
