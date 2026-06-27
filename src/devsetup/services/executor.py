import re
import subprocess
import shutil
from typing import Optional
from core.registry import VERSION_COMMANDS, SYSTEM_OS


class SystemExecutor:
    @staticmethod
    def extract_version(text: str) -> Optional[str]:
        match = re.search(r"\d+(?:\.\d+)+", text)
        return match.group(0) if match else None

    @classmethod
    def check_tool_status(cls, tool_name: str) -> tuple[bool, Optional[str]]:
        if (
            tool_name not in VERSION_COMMANDS
            or SYSTEM_OS not in VERSION_COMMANDS[tool_name]
        ):
            return False, None

        cmd = list(VERSION_COMMANDS[tool_name][SYSTEM_OS])
        resolved_path = shutil.which(cmd[0])
        if not resolved_path:
            return False, None

        cmd[0] = resolved_path

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                output = result.stdout.strip() or result.stderr.strip()
                return True, cls.extract_version(output)
            else:
                if result.stderr.strip():
                    version = cls.extract_version(result.stderr.strip())
                    if version:
                        return True, version
                return False, None
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False, None
