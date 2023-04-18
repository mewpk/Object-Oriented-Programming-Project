from fastapi import FastAPI
from .routers import  users, Course , Coupon,Categories,Order,StudentCourse,Review

app = FastAPI()

app.include_router(users.router)
app.include_router(Course.router)
app.include_router(Coupon.router)
app.include_router(Categories.router)
app.include_router(Order.router)
app.include_router(StudentCourse.router)
app.include_router(Review.router)

@app.get("/")
async def read_root():
    return {"message": "Yo!!! it's PookkiePraewa right here!!!!"}
