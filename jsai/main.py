from pprint import pprint

from jsai.core.runtime import create_registry


def main() -> None:
    registry = create_registry()

    print("JSAI Core v0.1")
    print("=" * 40)

    print("\nAvailable tools:")

    for tool in registry.list_tools():
        print(
            f"- {tool.name} "
            f"[{tool.risk.value}] "
            f"- {tool.description}"
        )

    print("\nExecuting system_info...\n")

    result = registry.execute("system_info")
    pprint(result)


if __name__ == "__main__":
    main()
