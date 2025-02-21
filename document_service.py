from app.config.database import db
from datetime import datetime

def save_analysis_result(doc_id, analysis, recommendations):
    db.analysis_results.insert_one({
        "doc_id": doc_id,
        "clauses": analysis,
        "recommendations": recommendations,
        "created_at": datetime.utcnow(),
    })



def get_analysis_result(doc_id):
    return db.analysis_results.find_one({"doc_id": doc_id})


def get_recommendations(doc_id):
    result = db.analysis_results.find_one({"doc_id": doc_id})
    return result.get("recommendations", [])
