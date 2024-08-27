from fastapi import FastAPI
import random
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/testeinicial")
async def root():
    return {"It's working!"}

@app.get("/numeroAle")
async def root():
    return {"Seu número é:": random.randint(1, 100)}