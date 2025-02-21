from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload, report, recommendations

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],  # This must allow OPTIONS implicitly!
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(report.router)
app.include_router(recommendations.router)


@app.on_event("shutdown")
async def shutdown():
    # Ensure tasks are awaited and closed cleanly
    print("Shutting down gracefully")

@app.get("/")
def home():
    return {"message": "Legal Document Analyzer Backend is Running!"}



