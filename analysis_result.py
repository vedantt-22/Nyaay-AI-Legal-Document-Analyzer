from pydantic import BaseModel
from typing import List, Dict


class AnalysisResult(BaseModel):
    doc_id: str
    clauses: List[Dict]
    recommendations: List[str]
