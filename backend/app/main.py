from fastapi import FastAPI
from .routers import  Users, Course , Coupon

app = FastAPI()

app.include_router(Users.router)
app.include_router(Course.router)
app.include_router(Coupon.router)

@app.get("/")
async def read_root():
    return {"message": "Yo!!! it's PW right here!!!!"}
