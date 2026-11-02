from agents.llm import ask


def research_agent(question):
    prompt = f"""
    Create a research plan for this question:

    {question}

    Return:
    1. A refined research question.
    2. Four specific subquestions.
    3. Three methods for investigating the topic.
    4. Two possible limitations.
    5. A suggested first step.

    Do not invent citations or claim you searched the web.
    """

    return ask(
        prompt,
        system=(
            "You are a research planning agent. "
            "Break complex questions into manageable tasks. "
            "Be specific and distinguish suggestions from facts."
        ),
    )


if __name__ == "__main__":
    question = input("Research question: ")
    print("\n=== RESEARCH PLAN ===\n")
    print(research_agent(question))
