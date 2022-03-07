from fastapi import FastAPI
from deta import App

# Our custom imports
from application.routers.shortener_endpoints import router as shortening_router
from application.utils import APP_VERSION, APP_TITLE

app = App(FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description="Simple URL shortener based on Deta"
))


@app.get('/')
def index():
    return {"response": f"System v{APP_VERSION} online!"}


app.include_router(shortening_router)
