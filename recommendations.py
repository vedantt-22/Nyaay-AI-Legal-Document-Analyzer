from fastapi import APIRouter, HTTPException
from app.services.document_service import get_recommendations

router = APIRouter()


@router.get("/recommendations/{doc_id}")
def get_recommendations_route(doc_id: str):
    recommendations = get_recommendations(doc_id)

    if not recommendations:
        raise HTTPException(status_code=404, detail="Document not found")

    return {"doc_id": doc_id, "recommendations": recommendations}
