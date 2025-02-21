from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="nlpaueb/legal-bert-base-uncased")

SAMPLE_QUESTIONS = [
    "What are the payment obligations?",
    "What are the delivery terms and timelines?",
    "Are there any termination clauses mentioned?",
    "Are there any penalties or liquidated damages specified?",
    "Are there any indemnity or liability clauses?",
    "Are there confidentiality or non-disclosure obligations?",
    "Are there dispute resolution clauses?",
    "What is the governing law for the contract?",
    "Are there any force majeure clauses?",
    "Are there obligations regarding intellectual property rights?"
]



def analyze_text_with_model(text):
    analysis = []
    for question in SAMPLE_QUESTIONS:
        result = qa_pipeline(question=question, context=text)
        analysis.append({
            "question": question,
            "answer": result["answer"],
            "score": result["score"],
        })
    return analysis
