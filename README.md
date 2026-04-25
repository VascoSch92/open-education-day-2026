# Beyond Black Boxes: Public AI for Open Education

Workshop example using [OpenHands](https://github.com/All-Hands-AI/OpenHands) + [Apertus-70B](https://huggingface.co/swiss-ai) via the [Public AI Inference Utility](https://publicai.co).

An AI tutor that reads your lecture materials and quizzes you on them.

## Setup

0. Prepare the environment

To run the demo, you will need a recent Python version and the 
[uv](https://github.com/astral-sh/uv) package manager.
You can use the attached Dev Container with your favorite IDE.

1. Install dependencies:

```bash
uv sync
```

2. Get a free API key at <https://platform.publicai.co> and export it:

```bash
export PUBLICAI_API_KEY="your-key-here"
```

3. Drop your lecture materials (PDF, markdown, text) next to `main.py`.

## Usage

```bash
uv run python main.py
```

Type `exit` or press `Ctrl-C` to quit.

## Customisation

Edit `tutor_prompt.j2` to change the agent's behaviour entirely.
