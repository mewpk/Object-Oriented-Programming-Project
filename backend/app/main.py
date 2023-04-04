from fastapi import FastAPI
from .routers import products, orders, Users

app = FastAPI()

app.include_router(Users.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
async def read_root():
    return {"message": "Yo!!! it's PW right here!!!!"}
