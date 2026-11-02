from agents.research_agent import research_agent
from agents.tool_agent import tool_agent
from agents.reflection_agent import reflection_agent


def main():
    print("\n=== AGENTIC AI LAB ===")
    print("1. Research Agent")
    print("2. Tool-Using Agent")
    print("3. Reflection Agent")

    choice = input("\nChoose an agent (1-3): ").strip()
    task = input("Enter your task: ").strip()

    if not task:
        print("Please enter a task.")
        return

    if choice == "1":
        result = research_agent(task)
        print("\n=== RESEARCH PLAN ===\n")
        print(result)

    elif choice == "2":
        result = tool_agent(task)
        print("\n=== TOOL AGENT RESULT ===\n")
        print(result)

    elif choice == "3":
        result = reflection_agent(task)

        print("\n=== FIRST DRAFT ===\n")
        print(result["draft"])

        print("\n=== CRITIQUE ===\n")
        print(result["critique"])

        print("\n=== REVISED ANSWER ===\n")
        print(result["revision"])

    else:
        print("Invalid choice. Select 1, 2, or 3.")


if __name__ == "__main__":
    main()
