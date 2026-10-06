from __future__ import annotations

from typing import Any
from jsai.security.authorization import authorize, AuthorizationDecision
from jsai.core.models import Tool

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
        decision = authorize(tool)


        if decision == AuthorizationDecision.REQUIRE_APPROVAL:
            raise PermissionError(
                f"Tool '{name}' requires user approval before execution."
            )

        if decision == AuthorizationDecision.DENY:
            raise PermissionError(
                f"Tool '{name}' is denied by security policy."
            )

        return tool.function(**kwargs)

