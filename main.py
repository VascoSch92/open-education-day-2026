"""
Minimal terminal chat with OpenHands — workshop example for
"Beyond Black Boxes: Public AI for Open Education".

Workflow:
  1. Edit system_prompt.txt to change the agent's behaviour.
  2. Run this script and chat with the agent.
  3. Type 'exit' (or Ctrl-C) to quit.

Model: Apertus-70B-Instruct via the Public AI Inference Utility
       (OpenAI-compatible endpoint — OpenHands talks to it via LiteLLM).
"""

import os
from pathlib import Path

from openhands.sdk import LLM, Agent, Conversation
from pydantic import SecretStr

# Path to the file containing the agent's system prompt.
# Edit this file to change how the agent behaves.
SYSTEM_PROMPT_FILE = Path(__file__).parent / "system_prompt.txt"


def main() -> None:

    # Connect to Apertus-70B via the Public AI inference endpoint.
    llm = LLM(
        usage_id="tutor",
        model="openai/swiss-ai/apertus-70b-instruct",
        api_key=SecretStr(os.environ["PUBLICAI_API_KEY"]),
        base_url="https://api.publicai.co/v1",
        max_input_tokens=128000,
        max_output_tokens=4096,
        extra_headers={"User-Agent": "open-education-day-2026"},
    )

    # Build the agent with the system prompt given in tutor_prompt.j2
    agent = Agent(
        llm=llm,
        system_prompt_filename=str(Path(__file__).parent / "tutor_prompt.j2"),
        tools=[],
    )

    # Create the conversation you will have with the agent
    # it will be saved under the directory conversation
    conversation = Conversation(
        agent=agent,
        workspace=str(Path(__file__).parent),
        persistence_dir=Path.cwd() / "conversations",
    )

    # Interactive chat loop.
    print("\n" + "=" * 60)
    print("  Chat with your Apertus tutor. Type 'exit' to quit.")
    print("=" * 60 + "\n")

    while True:
        try:
            user_input = input("you > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit", "bye"}:
            print("bye!")
            break

        conversation.send_message(user_input)
        conversation.run()

    conversation.close()


if __name__ == "__main__":
    main()
