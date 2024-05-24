# llmchat & llm-cli:
<p>Ths repository contains GUI LLM Chat App & also cli based chat app</p>

# llmchat:
<p>This is a WebUI APP written in python3 using the ollama and streamlit modules to chat with LLms running on your local machine :)</p>

![llmchat](https://github.com/Bhartiya-Hacker/llmchat/assets/108232080/5b5e7784-1e85-4ca0-a55b-6acd4286be6b)

# llm-cli:
<p>This is cli based chat app to chat with LLM running on your system</p>

![cli](https://github.com/Bhartiya-Hacker/llmchat/assets/108232080/a92d1840-0a9a-407b-9300-5cd83e0e943e)

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
<p>This will start server on localhost:8501 and open your web browsers</p>

# How to use CLI based Chat App:

```bash
python3 llm-cli.py
```
