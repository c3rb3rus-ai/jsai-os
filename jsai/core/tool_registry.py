from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Callable, Any


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
    requires_permission: bool


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ValueError(f"Tool already registered: {tool.name}")

        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool:
        if name not in self._tools:
            raise KeyError(f"Unknown tool: {name}")

        return self._tools[name]

    def list_tools(self) -> list[Tool]:
        return list(self._tools.values())

    def execute(self, name: str, **kwargs: Any) -> Any:
        tool = self.get(name)

        if tool.requires_permission:
            raise PermissionError(
                f"Tool '{name}' requires user permission before execution."
            )

        return tool.function(**kwargs)
