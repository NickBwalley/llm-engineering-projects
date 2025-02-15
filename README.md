# LLM Engineering Projects

Join me as I build innovative and exciting projects using large language models like GPT-4o, Claude 3.5 Sonnet, LLaMA, and other state-of-the-art LLMs. I will integrate these models with the powerful Gradio framework and later explore advanced projects that leverage Retrieval-Augmented Generation (RAG) and fine-tuning techniques to train models for domain-specific knowledge.

In these projects, we will focus on developing intelligent chatbots that can answer questions based on a customized knowledge base. We will also explore concepts such as vector embeddings and vector databases, which are crucial for optimizing retrieval processes.

These projects are not only insightful but also incredibly fun—so be sure to check them out! 😜😜

## first let's set up llama to run on our local machine.

We will start by installing Ollama so you can see results immediately!

1. Download and install Ollama from https://ollama.com noting that on a PC you might need to have administrator permissions for the install to work properly
2. On a PC, start a Command prompt / Powershell (Press Win + R, type `cmd`, and press Enter). On a Mac, start a Terminal (Applications > Utilities > Terminal).
3. Run `ollama run llama3.2` or for smaller machines try `ollama run llama3.2:1b` - **please note** steer clear of Meta's latest model llama3.3 because at 70B parameters that's way too large for most home computers!
4. If this doesn't work, you may need to run `ollama serve` in another Powershell (Windows) or Terminal (Mac), and try step 3 again
5. And if that doesn't work on your box, I've set up this on the cloud. This is on Google Colab, which will need you to have a Google account to sign in, but is free: https://colab.research.google.com/drive/1-_f5XZPsChvfU1sJ0QqCePtIuc55LSdu?usp=sharing

## Setting up your LLM Development Environment Tools and Best Practices.

```
mkdir <llm_engineering>
cd <path/llm_engineering/>
conda env create -f environment.yml
conda activate llms
jupyter lab

```
