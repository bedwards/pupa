### Pupa

Local literary translation pipeline for large language models.

#### Overview

Pupa is a lightweight script designed to automate chapter-by-chapter literary translation using locally hosted large language models through Ollama. It reads a text file containing a Chinese novel, segments it by chapter markers, and sends each section as a styled translation prompt—here, explicitly asking the model to render the prose in the voice of Colson Whitehead. By delegating to models such as Qwen2.5:72b or Llama3.3:70b, it allows for flexible experimentation with tone and model behavior while maintaining full local control over data and inference.

The scripts are written in Python and rely on the system’s Ollama installation rather than a cloud API, keeping the translation process offline and model-agnostic. Its purpose is practical and exploratory: to benchmark literary translation workflows, test stylistic consistency across long texts, and serve as a repeatable structure for larger translation projects.
