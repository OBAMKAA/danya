from fastapi import FastAPI, Response, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="../public"), name="public")


@app.get("/")
async def root():
    with open('/public/index.html', '/public/about.html') as file:
        data = file.read()
    return Response(content=data, media_type="text/html")
@app.get("/public/about.html")
def about():
    return {"message": "..."}

#@app.get('/data')
#Request.get(Request.)