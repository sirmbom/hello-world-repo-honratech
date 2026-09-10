from fastapi import FastAPI, UploadFile, Form, File
from typing import Optional
from pydantic import BaseModel

app = FastAPI(title="New Instance")

@app.post("/test")
def test_point(file: UploadFile = File(...), status: bool = Form(default=True)):
    return {"file": file, "status": status}