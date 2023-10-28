from fastapi import FastAPI

app = FastAPI()

#home route
@app.get("/")
def read_root():
    return {"Hello": "World"}
# added comments
# changed comments
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = ""):  
    return {"item_id": item_id, "q": q}