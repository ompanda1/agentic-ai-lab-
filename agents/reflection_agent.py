from agents.llm import ask


def reflection_agent(task):
    # Stage 1: Generate an initial answer.
    draft = ask(
        task,
        system=(
            "You are a helpful assistant. "
            "Write a clear first draft that answers the task."
        ),
    )

    # Stage 2: Critique the draft.
    critique = ask(
        f"""
        Review this draft for:
        1. Unsupported claims or possible inaccuracies
        2. Missing reasoning
        3. Clarity and relevance

        Original task:
        {task}

        Draft:
        {draft}

        Identify specific weaknesses and suggest improvements.
        Do not invent facts or claim to have verified anything.
        """,
        system=(
            "You are a critical reviewer. "
            "Give specific, constructive feedback."
        ),
    )

    # Stage 3: Revise using the critique.
    revision = ask(
        f"""
        Improve the draft using the critique.

        Original task:
        {task}

        First draft:
        {draft}

        Critique:
        {critique}

        Produce a clear final answer. Correct weaknesses where
        possible, and acknowledge uncertainty where appropriate.
        """,
        system=(
            "You revise answers based on feedback. "
            "Do not add unsupported claims."
        ),
    )

    return {
        "draft": draft,
        "critique": critique,
        "revision": revision,
    }


if __name__ == "__main__":
    task = input("What should the agent answer? ")
    result = reflection_agent(task)

    print("\n=== FIRST DRAFT ===\n")
    print(result["draft"])

    print("\n=== CRITIQUE ===\n")
    print(result["critique"])

    print("\n=== REVISED ANSWER ===\n")
    print(result["revision"])
