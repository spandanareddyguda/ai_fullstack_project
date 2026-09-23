import ollama
question=input("Ask your question: ")
response = ollama.chat(
    model="llama3.2.:3b",
    messages=[
        {
            "role": "system",
            "content": "give answers in two lines only "
        },
        {
            "role":"user",
            "content": question
        }
    ]
)
print(response['message']['content'])