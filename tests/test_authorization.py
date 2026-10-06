from jsai.core.models import RiskLevel, Tool
from jsai.security.authorization import AuthorizationDecision, authorize


def fake_tool(risk: RiskLevel) -> Tool:
    return Tool(
        name="test_tool",
        description="Tool used for authorization testing.",
        function=lambda: None,
        risk=risk,
    )


def test_authorization_policy() -> None:
    assert authorize(fake_tool(RiskLevel.READ_ONLY)) == AuthorizationDecision.ALLOW

    assert (
        authorize(fake_tool(RiskLevel.USER_CHANGE))
        == AuthorizationDecision.REQUIRE_APPROVAL
    )

    assert (
        authorize(fake_tool(RiskLevel.SYSTEM_CHANGE))
        == AuthorizationDecision.REQUIRE_APPROVAL
    )

    assert authorize(fake_tool(RiskLevel.HIGH_RISK)) == AuthorizationDecision.DENY
