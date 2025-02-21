from fastapi import APIRouter, UploadFile, File
import uuid
from app.utils.text_extractor import extract_text_from_pdf
from app.services.model_service import analyze_text_with_model
from app.services.document_service import save_analysis_result
from datetime import datetime

router = APIRouter()

def generate_recommendations(analysis):
    recommendations = []

    for item in analysis:
        question = item["question"].lower()
        answer = item["answer"].lower()

        if "payment obligations" in question and "30 days" not in answer:
            recommendations.append("Clarify the payment terms, ensure they specify exact deadlines.")
        
        if "termination" in question and "not mentioned" in answer:
            recommendations.append("Consider adding a termination clause to avoid future disputes.")

        if "penalties" in question and "not mentioned" in answer:
            recommendations.append("Consider including penalty terms for non-performance.")

        if "indemnity" in question and "not mentioned" in answer:
            recommendations.append("Review if indemnity obligations need to be added for risk coverage.")

        if "dispute resolution" in question and "not mentioned" in answer:
            recommendations.append("Include dispute resolution terms (e.g., arbitration) for conflict management.")

    if not recommendations:
        recommendations.append("No critical issues detected, but consider a legal review for finer details.")

    return recommendations


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    doc_id = str(uuid.uuid4())

    # Extract text from PDF
    text = extract_text_from_pdf(file.file)

    # Analyze with LegalBERT
    analysis = analyze_text_with_model(text)

    # Generate Recommendations
    recommendations = generate_recommendations(analysis)

    # Save to database
    save_analysis_result(doc_id, analysis, recommendations)

    return {
        "message": "Document uploaded and analyzed successfully",
        "doc_id": doc_id,
        "analysis_summary": [f"{item['question']} → {item['answer']}" for item in analysis],
        "recommendations": recommendations,
    }
