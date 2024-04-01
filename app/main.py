
#import sys
#sys.path.append("..")

from fastapi import FastAPI
from starlette.responses import HTMLResponse
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast Blog API",
    description="A simple blog API using FastAPI",
    version="0.0.1",
)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

@app.get("/", response_class=HTMLResponse)
def index():
    return """
        <html>
            <body>
                <h1>FAST BLOG API</h1>
                <h3>v0.3.0</h3>

                <strong>Documentation</strong>: <a href="/docs">OpenAPI</a>
            </body>
        </html>
    """
