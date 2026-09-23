import ollama
while True:
    question = input("Ask your question: ")
    if question.lower() == "exit":
        break
    response = ollama.chat(
        model="llama3.2.:3b",
        messages=[
            {
                "role": "system",
                "content": "give answer in two lines only "
            },
            {
                "role":"user",
                "content":question
            }
        ]
    )
    print(response['message']['content'])