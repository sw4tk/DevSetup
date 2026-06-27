import os
import json
from datetime import datetime
from typing import List, Dict, Tuple
from core.models import Profile, ToolStatus
from services.executor import SystemExecutor


class ProfileService:
    BASE_DIR = "profiles"
    CATEGORIES = ["custom", "builtins", "imports"]
    LOCAL_FILENAME = ".devsetup.json"

    @classmethod
    def init_storage(cls):
        for cat in cls.CATEGORIES:
            os.makedirs(os.path.join(cls.BASE_DIR, cat), exist_ok=True)

    @classmethod
    def locate_profile(cls, name: str) -> str:
        possible_bases = ["profiles", "profile"]
        possible_cats = [
            "custom",
            "customs",
            "builtin",
            "builtins",
            "imports",
            "import",
        ]

        for base in possible_bases:
            for cat in possible_cats:
                path = os.path.join(base, cat, f"{name}.json")
                if os.path.exists(path):
                    return path
        raise FileNotFoundError(f"Profile '{name}' not found.")

    @classmethod
    def _parse_tools(cls, raw_tools: list) -> Tuple[List[str], List[Dict]]:
        parsed_tools, frozen_data = [], []
        for t in raw_tools:
            if isinstance(t, dict):
                parsed_tools.append(t.get("name", "unknown"))
                frozen_data.append(t)
            else:
                parsed_tools.append(str(t))
                frozen_data.append({"name": str(t), "version": None})
        return parsed_tools, frozen_data

    @classmethod
    def load(cls, name: str) -> Profile:
        path = cls.locate_profile(name)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            parsed_tools, frozen_data = cls._parse_tools(data.get("tools", []))
            return Profile(
                name=data.get("name", name),
                description=data.get("description", ""),
                tools=parsed_tools,
                is_freezed=data.get("is_freezed", False),
                frozen_tools=frozen_data,
                devsetup_version=data.get("devsetup_version", "1.0.0"),
                date_created=data.get("date"),
            )

    @classmethod
    def save(cls, profile: Profile, category: str = "custom"):
        cls.init_storage()
        path = os.path.join(cls.BASE_DIR, category, f"{profile.name}.json")
        cls._write_json(path, profile)

    @classmethod
    def load_local(cls) -> Profile:
        """Loads the .devsetup.json from the current working directory."""
        if not os.path.exists(cls.LOCAL_FILENAME):
            raise FileNotFoundError(
                f"No {cls.LOCAL_FILENAME} found in current directory. Run 'devsetup init' first."
            )

        with open(cls.LOCAL_FILENAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            parsed_tools, frozen_data = cls._parse_tools(data.get("tools", []))
            return Profile(
                name=data.get("name", "local-project"),
                description=data.get("description", "Local project environment"),
                tools=parsed_tools,
                is_freezed=data.get("is_freezed", False),
                frozen_tools=frozen_data,
                devsetup_version=data.get("devsetup_version", "1.0.0"),
                date_created=data.get("date"),
            )

    @classmethod
    def save_local(cls, profile: Profile):
        """Saves a profile to .devsetup.json in the current working directory."""
        cls._write_json(cls.LOCAL_FILENAME, profile)

    @classmethod
    def _write_json(cls, path: str, profile: Profile):
        out_tools = profile.tools if not profile.is_freezed else profile.frozen_tools
        payload = {
            "name": profile.name,
            "description": profile.description,
            "is_freezed": profile.is_freezed,
            "tools": out_tools,
            "devsetup_version": profile.devsetup_version,
            "date": profile.date_created
            or datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4)

    @classmethod
    def scan_profile(
        cls, profile: Profile, progress_callback=None
    ) -> Tuple[List[ToolStatus], List[str]]:
        installed, missing = [], []
        for idx, tool in enumerate(profile.tools):
            if progress_callback:
                progress_callback(tool, idx, len(profile.tools))
            status, version = SystemExecutor.check_tool_status(tool)
            if status:
                installed.append(ToolStatus(name=tool, installed=True, version=version))
            else:
                missing.append(tool)
        return installed, missing

    @classmethod
    def list_all(cls) -> Dict[str, List[str]]:
        cls.init_storage()
        result = {}
        for base in ["profiles", "profile"]:
            if not os.path.exists(base):
                continue
            for cat in [
                "custom",
                "customs",
                "builtin",
                "builtins",
                "imports",
                "import",
            ]:
                folder = os.path.join(base, cat)
                if os.path.exists(folder):
                    files = [
                        os.path.splitext(f)[0]
                        for f in os.listdir(folder)
                        if f.endswith(".json")
                    ]
                    if files:
                        display_cat = cat.rstrip("s") if cat != "imports" else cat
                        result.setdefault(display_cat, []).extend(files)
        return {k: list(set(v)) for k, v in result.items()}

    @classmethod
    def export_profile(
        cls, name: str, freeze: bool = False, output_dir: str = "exports"
    ):
        os.makedirs(output_dir, exist_ok=True)
        profile = cls.load(name)
        if freeze:
            installed, _ = cls.scan_profile(profile)
            profile.is_freezed = True
            profile.frozen_tools = [
                {"name": t.name, "version": t.version} for t in installed
            ]
            profile.tools = [t.name for t in installed]
        path = os.path.join(output_dir, f"{profile.name}_export.json")
        cls._write_json(path, profile)
        return path

    @classmethod
    def import_profile(cls, filepath: str):
        if not os.path.exists(filepath):
            raise FileNotFoundError("File not found.")
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        parsed_tools, frozen_data = cls._parse_tools(data.get("tools", []))
        profile = Profile(
            name=data.get("name", "Imported"),
            description=data.get("description", ""),
            tools=parsed_tools,
            is_freezed=data.get("is_freezed", False),
            frozen_tools=frozen_data,
            devsetup_version="1.0.0",
            date_created=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        )
        cls.save(profile, category="imports")
        return profile.name
