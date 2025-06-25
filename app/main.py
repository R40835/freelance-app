from fastapi import FastAPI
from app import crud, schemas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)


@app.post("/customers", response_model=schemas.CustomerOut)
async def create_customer(customer: schemas.CustomerCreate):
    return await crud.create_customer(customer)


@app.get("/customers", response_model=list[schemas.CustomerOut])
async def list_customers():
    return await crud.get_customers()