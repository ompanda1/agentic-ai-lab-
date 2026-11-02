import json

from agents.llm import ask
from tools.calculator import calculate


def tool_agent(task):
    decision_prompt = f"""
    Decide how to handle this task:

    {task}

    Return exactly one JSON object.

    If arithmetic is needed:
    {{"action": "calculate", "expression": "1247 * 38"}}

    Otherwise:
    {{"action": "answer", "answer": "your response"}}

    Only use basic arithmetic in calculator expressions.
    Do not include Python code.
    """

    decision = ask(
        decision_prompt,
        system=(
            "You are a tool-using agent. "
            "Choose the calculator for arithmetic tasks. "
            "Return valid JSON only."
        ),
    )

    try:
        start = decision.find("{")
        end = decision.rfind("}") + 1

        if start == -1 or end <= start:
            raise ValueError("No JSON found")

        result = json.loads(decision[start:end])

    except (json.JSONDecodeError, ValueError):
        return f"Could not parse the model's decision:\n{decision}"

    action = result.get("action")

    if action == "calculate":
        expression = result.get("expression")

        if not isinstance(expression, str):
            return "Invalid calculator expression."

        try:
            value = calculate(expression)
        except (
            ValueError,
            SyntaxError,
            ZeroDivisionError,
            OverflowError,
        ):
            return "The calculator rejected the expression."

        print(f"\nTool selected: calculator")
        print(f"Expression: {expression}")
        print(f"Verified calculation result: {value}")

        return ask(
            f"The calculator computed {expression} = {value}. "
            "Explain the result briefly using this computed value.",
            system="Explain the supplied calculation accurately.",
        )

    if action == "answer":
        return str(result.get("answer", "No answer provided."))

    return f"Unknown action: {action}"


if __name__ == "__main__":
    task = input("Enter a task: ")
    print("\n=== TOOL AGENT RESULT ===\n")
    print(tool_agent(task))
