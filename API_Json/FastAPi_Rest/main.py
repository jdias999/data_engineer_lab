from fastapi import FastAPI

app = FastAPI()  # uvicorn main:app --reload

from auth_routes import auth_router
from order_routes import order_rounter

app.include_router(auth_router)
app.include_router(order_rounter)