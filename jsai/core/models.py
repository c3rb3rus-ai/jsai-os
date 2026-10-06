from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable


class RiskLevel(Enum):
    READ_ONLY = "read_only"
    USER_CHANGE = "user_change"
    SYSTEM_CHANGE = "system_change"
    HIGH_RISK = "high_risk"


@dataclass
class Tool:
    name: str
    description: str
    function: Callable[..., Any]
    risk: RiskLevel
