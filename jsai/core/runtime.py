from jsai.core.models import RiskLevel, Tool
from jsai.core.tool_registry import ToolRegistry
from jsai.tools.system_info import get_system_info


def create_registry() -> ToolRegistry:
    registry = ToolRegistry()

    registry.register(
        Tool(
            name="system_info",
            description="Inspect basic information about the computer.",
            function=get_system_info,
            risk=RiskLevel.READ_ONLY,
        )
    )

    return registry
