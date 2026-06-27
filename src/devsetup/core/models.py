from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any


@dataclass
class ToolStatus:
    name: str
    installed: bool
    version: Optional[str] = None


@dataclass
class Profile:
    name: str
    description: str
    tools: List[str] = field(default_factory=list)
    is_freezed: bool = False
    frozen_tools: List[Dict[str, Any]] = field(default_factory=list)
    devsetup_version: str = "1.0.0"
    date_created: Optional[str] = None
