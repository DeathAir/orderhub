from fastapi import FastAPI

from app.api.routers.orders import router as orders_router

app = FastAPI()

app.include_router(orders_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"status": "Ok"}