from fastapi import FastAPI
app = FastAPI()
@app.get("/aTeste")
async def root():
    return {"message": "Hello World"}

@app.get("/aTeste1")
async def root():
    return {"message": "It's Working"}