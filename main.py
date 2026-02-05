from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts = [
    {
        "id": "1",
        "author": "Tarun Tehri",
        "title": "Dummy post",
        "content": "fast api framework",
        "date_posted": "Feb 1, 2026",
    },
    {
        "id": "2",
        "author": "Divya Tehri",
        "title": "Another dummy post",
        "content": "fast api framework",
        "date_posted": "Feb 2, 2026",
    },
    {
        "id": "3",
        "author": "Kiaan Tehri",
        "title": "Yet another post",
        "content": "Best post yet",
        "date_posted": "Feb 5,2026",
    },
]


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"},
    )


# API Routes
@app.get("/api/posts")
def get_posts():
    return posts
