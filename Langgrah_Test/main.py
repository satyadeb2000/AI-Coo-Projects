from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return JSONResponse(content={"status": "healthy"})

@app.get("/")
def root():
    return RedirectResponse(url="/docs") 