import json


from chatbot import unhelpful_chat


def evaluate(messages: list[dict[str, str]]) -> dict[str, float]:
    pass


def main():
    messages = unhelpful_chat()
    scores = evaluate(messages)
    print(json.dumps(scores, indent=4))


if __name__ == "__main__":
    main()
