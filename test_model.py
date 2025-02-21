from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="pile-of-law/legalbert-large-1.7M-2")

context = """
The Supplier shall deliver the products within 30 days of receiving the order. In case of delays, a penalty of 5% shall apply.
"""

question = "What are the delivery terms?"

result = qa_pipeline(question=question, context=context)

print("Question:", question)
print("Answer:", result['answer'])
print("Score:", result['score'])
