from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from starlette.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
port = 8000
app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/tree")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("tree.html", {"request": request})


@app.get("/end")
def read_root(request: Request):
    return templates.TemplateResponse("end.html", {"request": request})



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
    print(f"Running on localhost: {port}")
