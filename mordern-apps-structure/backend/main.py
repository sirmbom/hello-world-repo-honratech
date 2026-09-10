from fastapi import FastAPI

from fastapi_advanced.app import app as profile_router
from fastapi_advanced.app2 import app as product_router
from first_app import app as multi_router

app = FastAPI(title="Route Database")

app.include_router(profile_router)
app.include_router(product_router)
app.include_router(multi_router)

@app.get("/") # Decorator - @ # HTTP method: GET, POST
def home(action: str):
    """ This endpoint is used to expose the root. It needs an action parameter. """ # Docstring
    return {"status": "online", "system": "Hello World", "action": action}