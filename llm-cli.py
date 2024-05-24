import requests
import json
import os
import datetime

def chat_with_tinyllama(prompt):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "tinyllama",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": True
    }
    response = requests.post(url, json=payload, stream=True)
    
    return response

def main():
    conversation = []  # List to store conversation history

    print("You can start chatting with TinyLlama now. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            save_conversation = input("Do you want to save the conversation? (yes/no): ").lower()
            if save_conversation == 'yes':
                filename = input("Enter the filename to save the conversation: ")
                if not filename.endswith('.txt'):
                    filename += '.txt'
                with open(filename, 'w') as file:
                    for message in conversation:
                        file.write(message + '\n')
                print(f"Conversation saved to {filename}")
            break
        
        response = chat_with_tinyllama(user_input)
        print("TinyLlama: ", end="", flush=True)
        
        complete_message = ""
        for line in response.iter_lines():
            if line:
                message = json.loads(line.decode('utf-8'))
                if message["message"]["role"] == "assistant":
                    chunk = message["message"]["content"]
                    complete_message += chunk
                    print(chunk, end="", flush=True)
        
        print()  # For a new line after the complete response
        conversation.append(f"You: {user_input}")
        conversation.append(f"TinyLlama: {complete_message}")

if __name__ == "__main__":
    main()
