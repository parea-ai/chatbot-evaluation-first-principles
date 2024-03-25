from utils import call_openai


def goal_success_ratio(messages: list) -> float:
    pass


def friendliness(output: str) -> float:
    response = call_openai(
        [
            {"role": "system", "content": "You evaluate the friendliness of the following response on a scale of 0 to 10. You must only return a number."},
            {"role": "assistant", "content": output},
        ],
        model="gpt-4",
    )
    try:
        return float(response) / 10.0
    except TypeError:
        return 0.0


def usefulness(user_input: str, output: str) -> float:
    response = call_openai(
        [
            {"role": "system", "content": "You evaluate the usefulness of the response given the user input on a scale of 0 to 10. You must only return a number."},
            {"role": "assistant", "content": f'''User input: "{user_input}"\nAssistant response: "{output}"'''},
        ],
        model="gpt-4",
    )
    try:
        return float(response) / 10.0
    except TypeError:
        return 0.0
