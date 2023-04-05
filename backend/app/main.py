from fastapi import FastAPI
from .routers import  Users, Course , Coupon,Categories

app = FastAPI()

app.include_router(Users.router)
app.include_router(Course.router)
app.include_router(Coupon.router)
app.include_router(Categories.router)

@app.get("/")
async def read_root():
    return {"message": "Yo!!! it's PookkiePraewa right here!!!!"}
