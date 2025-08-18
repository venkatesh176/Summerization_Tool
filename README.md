# 📝 Summarization Tool (LangChain + Gemma)

This project showcases a custom text summarization pipeline using LangChain and the locally hosted Gemma model via Ollama. It extracts structured story elements like title, overview, and conclusion from user prompts.

## 🚀 Features

- Built with `Flask` for a lightweight web interface
- Uses `LangChain` with `OllamaLLM` to run Gemma locally
- Outputs structured summaries using `pydantic` and `JsonOutputParser`
- Conda environment for isolated dependency management

## 🧠 How It Works

1. User submits a story topic (e.g., "India")
2. LangChain prompt template formats the query
3. Gemma model generates structured output
4. Output parsed into `title`, `overview`, and `conclusion`

## 🧰 Tech Stack

- `Flask` – web interface
- `LangChain` – prompt orchestration
- `OllamaLLM` – local model integration
- `Gemma` – LLM hosted locally
- `pydantic` – structured output parsing

## 📦 Setup

```bash
conda create -n gemma_env python=3.10
conda activate gemma_env
pip install -r requirements.txt
