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
        "profile_image": "https://api.dicebear.com/7.x/avataaars/svg?seed=Tarun",
    },
    {
        "id": "2",
        "author": "Divya Tehri",
        "title": "Another dummy post",
        "content": "fast api framework",
        "date_posted": "Feb 2, 2026",
        "profile_image": "https://api.dicebear.com/7.x/avataaars/svg?seed=Divya",
    },
    {
        "id": "3",
        "author": "Kiaan Tehri",
        "title": "Yet another post",
        "content": "Best post yet",
        "date_posted": "Feb 5,2026",
        "profile_image": "https://api.dicebear.com/7.x/avataaars/svg?seed=Kiaan",
    },
]


@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
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
