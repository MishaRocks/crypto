from fastapi import FastAPI, HTTPException, Request
from services.coins import coins
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(
    docs_url=None,
    redoc_url=None,
)
templates = Jinja2Templates(directory="tmpl")


@app.get("/")
async def show_info(request: Request) -> HTMLResponse:
    r = coins()
    return templates.TemplateResponse(request, "coin-list.html",
                                      {"coins": r})
