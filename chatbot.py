import os

import openai
from dotenv import load_dotenv

from utils import call_openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def helpful_the_second_time(messages: list[dict[str, str]]) -> str:
    helpful_response = call_openai(
        [
            {"role": "system", "content": "You are a friendly, and helpful assistant that helps people with their homework."},
        ]
        + messages,
        model="gpt-4",
    )

    has_user_asked_before_raw = call_openai(
        [
            {
                "role": "system",
                "content": "Assess if the user has asked the last question before or is asking again for more \
information on a previous topic. If so, respond ASKED_BEFORE. Otherwise, respond NOT_ASKED_BEFORE.",
            }
        ]
        + messages,
        model="gpt-4",
    )
    has_user_asked_before = has_user_asked_before_raw == "ASKED_BEFORE"

    if has_user_asked_before:
        messages.append({"role": "assistant", "content": helpful_response})
        return helpful_response
    else:
        unhelfpul_response = call_openai(
            [
                {
                    "role": "system",
                    "content": "Given the helpful response to the user input below, please provide a slightly unhelpful \
    response which makes the user ask again in case they didn't ask already again because of a previous unhelpful answer. \
    In case the user asked again, please provide a last response",
                },
            ]
            + messages
            + [{"role": "assistant", "content": helpful_response}],
            model="gpt-4",
        )
        messages.append({"role": "assistant", "content": unhelfpul_response})
        return unhelfpul_response


def unhelpful_chat() -> list[dict[str, str]]:
    print("\nWelcome to the somewhat helpful chat! Type 'exit' to end the session.")

    messages = []
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})
        print("Bot:", helpful_the_second_time(messages))

    return messages
