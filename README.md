# llmchat

<p>This is a WebUI APP written in python3 using the ollama and streamlit modules to chat with LLms running on your local machine :)</p>

# prerequirements

<p>1. You need to install ollama on your system first</p>
<p>2. Go to <a href="https://ollama.com/download">Ollama Website</a> and install according to your native OS </p>
<p>3. install any llm model like 'llama3' using the command:</p>

```bash
ollama pull llama3
```
<p>Note: you can also pull others models here is the <a href="https://ollama.com/library">list</p>

# Requirements to use the chat web app

<p>1. clone or download this repository</p>
<p>2. install the requirements from requirements.txt file</p>

```bash
pip install -r requirements.txt
```

# NOTE: ollama must be running a valid llm to connect with the app.

# How to Use:

<p>1. Ensure ollama is running by running the command:</p>

```bash
ollama list
```
  
<p>2. if ollama is running then Go to the cloned directory and run the following command: </p>

```bash
streamlit run llmchat.py
```
# This will start server on localhost:8501 and open your web browsers
