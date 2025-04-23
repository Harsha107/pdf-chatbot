from chatbot_core import build_qa_chain

qa_chain = build_qa_chain("your_pdf.pdf")
chat_history = []

print("PDF-Chatbot started! Enter 'exit' to quit.")

while True:
    query = input("\nYour questions: ")
    if query.lower() in ["exit", "quit"]:
        print("Chat finished!")
        break

    result = qa_chain({"question": query, "chat_history": chat_history})
    print("\nAnswer:", result["answer"])
    chat_history.append((query, result["answer"]))
    print("\nSource - Document snippet:")
    print(result["source_documents"][0].page_content[:300])