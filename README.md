# Llama2-Blog-Generator

A Streamlit web app that generates short blog posts on a given topic using a locally-run, quantized Llama 2 model (`llama-2-7b-chat.ggmlv3.q8_0.bin`) via LangChain's `CTransformers` wrapper.

## How it works

`app.py`:

1. Presents a simple form: blog topic, desired word count, and target audience (`General Audience`, `Researchers`, or `Students`).
2. On submit, loads the local Llama 2 GGML model with `CTransformers` (`max_new_tokens=256`, `temperature=0.01`).
3. Fills a LangChain `PromptTemplate` — *"Write a blog for `{blog_style}` job profile for a topic `{input_text}` within `{no_of_words}` words."* — with the user's inputs.
4. Runs the prompt through the model and displays the generated blog text in the app.

## Project structure

- `app.py` — the Streamlit application (UI + generation logic).
- `requirements.txt` — Python dependencies.

## Requirements

```
langchain
sentence-transformers
uvicorn
streamlit
ctransformers
python-box
```

You will also need the quantized model file `llama-2-7b-chat.ggmlv3.q8_0.bin`, placed in a local `models/` folder (referenced in `app.py` as `models\llama-2-7b-chat.ggmlv3.q8_0.bin`). You can download compatible GGML Llama 2 model files from Hugging Face (e.g. TheBloke's Llama-2-7B-Chat-GGML repository).

## Setup & usage

```bash
pip install -r requirements.txt
# place llama-2-7b-chat.ggmlv3.q8_0.bin under models/
streamlit run app.py
```

Then open the app in your browser, enter a topic, word count, and audience, and click **Generate Blog**.

## Notes

- The model path in `app.py` uses a Windows-style path (`models\...`); update it to a forward-slash path (`models/...`) if running on macOS/Linux.
- Inference runs entirely locally/CPU via `ctransformers` — no external API key is required.
