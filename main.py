import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def root():
    return {'root': 'root'}


class ModelNested(BaseModel):
    val_nested1: int
    val_nested2: str

class ModelMain(BaseModel):
    val_main: int
    val_nested: ModelNested


@app.post('/model')
def model(item: ModelMain):
    return {'model': 'model'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
