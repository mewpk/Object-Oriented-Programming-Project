from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import  users, Course , Coupon,Categories,Order

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

@app.get("/")
async def read_root():
    return {"message": "Yo!!! it's PookkiePraewa right here!!!!"}
