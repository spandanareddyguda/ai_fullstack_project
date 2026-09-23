import ollama

response = ollama.chat(
    model='llama3', 
    messages=[
        {
            "role": "user",
            "content": "Name main types of Ai"
        }
    ]
)
print(response['message']['content'])