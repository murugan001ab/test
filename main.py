from fastapi import FastAPI,Query,Path
from pydantic import BaseModel,Field
app=FastAPI()


class user( ):
    name:str
    password:str
@app.get("/")
def dashboard():
    return {"message":"helo"}

@app.get("/items/{item_id}")
def get_item(item_id:int = Path(ge=0,le=100) )->dict:
    return {"item_id":item_id}



