from jsai.core.tool_registry import RiskLevel, Tool, ToolRegistry
from jsai.tools.system_info import get_system_info


def create_registry() -> ToolRegistry:
    registry = ToolRegistry()

    registry.register(
        Tool(
            name="system_info",
            description="Inspect basic information about the computer.",
            function=get_system_info,
            risk=RiskLevel.READ_ONLY,
            requires_permission=False,
        )
    )

    return registry
