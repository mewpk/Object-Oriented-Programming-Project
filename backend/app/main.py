from fastapi import FastAPI
from .routers import  users, Course , Coupon,Categories,Order,StudentCourse,Review,Favorite,Cart
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(users.router)
app.include_router(Course.router)
app.include_router(Coupon.router)
app.include_router(Categories.router)
app.include_router(Order.router)
app.include_router(StudentCourse.router)
app.include_router(Review.router)
app.include_router(Cart.router)
app.include_router(Favorite.router)


@app.get("/")
async def read_root():
    return {"message": "Yo!!! it's Pat Pookkie Praewa Mew right here!!!!"}
