from fastapi import FastAPI
from .routers import  Course , Coupon, Categories, users

app = FastAPI()

app.include_router(users.router)
app.include_router(Course.router)
app.include_router(Coupon.router)
app.include_router(Categories.router)
@app.get("/")
async def read_root():
    return {"message": "Yo!!! it's PW right here!!!!"}
