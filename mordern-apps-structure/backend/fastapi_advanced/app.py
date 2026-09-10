from fastapi import FastAPI, UploadFile, Form, File, APIRouter
from typing import Optional
from pydantic import BaseModel

app = APIRouter(prefix="/profile", tags=["Profile"])

@app.post("/test")
def test_point(file: UploadFile = File(...), status: bool = Form(default=True)):
    return {"file": file, "status": status}