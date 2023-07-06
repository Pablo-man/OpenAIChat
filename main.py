from fastapi import FastAPI
import uvicorn

from uce.ai.openuce import Document, process_inference

app = FastAPI()
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8053)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/inference", status_code=200)
def inference(doc: Document):
    tema = process_inference(doc.item)
    return {
        'respuesta': tema[0],
        'Tokens usados': tema[1]
    }
