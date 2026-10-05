from fastapi import FastAPI

app = FastAPI(
    title="PySentinel API",
    description="Status monitoring API for PySentinel",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "service": "PySentinel",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "PySentinel"
    }