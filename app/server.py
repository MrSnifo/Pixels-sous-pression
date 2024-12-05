from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from .api import upload  # Import your upload router

import os

app = FastAPI()

# Set the folder for static files
folder = os.path.dirname(__file__)

# Mount the static files (ensure your static directory exists)
app.mount("/static", StaticFiles(directory=os.path.join(folder, "static")), name="static")

# Templates directory for HTML files
templates = Jinja2Templates(directory=os.path.join(folder, "static"))

# Include your upload API router
app.include_router(upload.router, prefix="/api")

# Home route to serve your HTML template
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
