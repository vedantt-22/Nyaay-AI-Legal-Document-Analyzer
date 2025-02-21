from fastapi import APIRouter, HTTPException
from app.services.document_service import get_analysis_result

router = APIRouter()


@router.get("/report/{doc_id}")
def get_report(doc_id: str):
    result = get_analysis_result(doc_id)

    if not result:
        raise HTTPException(status_code=404, detail="Document not found")

    # Exclude `_id` from MongoDB response because it is not JSON serializable
    result.pop('_id', None)

    return result
