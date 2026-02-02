from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

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
        "author": "divya Tehri",
        "title": "Another dummy post",
        "content": "fast api framework",
        "date_posted": "Feb 2, 2026",
    },
]


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}<h1>"


@app.get("/api/posts")
def get_posts():
    return posts
