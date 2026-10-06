from __future__ import annotations

from enum import Enum

from jsai.core.models import RiskLevel, Tool


class AuthorizationDecision(Enum):
    ALLOW = "allow"
    REQUIRE_APPROVAL = "require_approval"
    DENY = "deny"


def authorize(tool: Tool) -> AuthorizationDecision:
    """Determine whether a tool may execute based on its risk level."""

    if tool.risk == RiskLevel.READ_ONLY:
        return AuthorizationDecision.ALLOW

    if tool.risk in (
        RiskLevel.USER_CHANGE,
        RiskLevel.SYSTEM_CHANGE,
    ):
        return AuthorizationDecision.REQUIRE_APPROVAL

    return AuthorizationDecision.DENY
