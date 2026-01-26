from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# Sample text posts dictionary
text_posts = {
    1: {
        "title": "Introduction to FastAPI",
        "content": "FastAPI is a modern, fast web framework for building APIs with Python."
    },
    2: {
        "title": "Python Best Practices",
        "content": "Writing clean and maintainable Python code is essential for long-term success."
    },
    3: {
        "title": "Database Design Tips",
        "content": "Proper database schema design can significantly improve application performance."
    },
    4: {
        "title": "API Security Fundamentals",
        "content": "Understanding authentication and authorization is crucial for API development."
    },
    5: {
        "title": "Async Programming in Python",
        "content": "Asynchronous programming allows for better handling of I/O-bound operations."
    },
    6: {
        "title": "Testing Your API",
        "content": "Comprehensive testing ensures your API works correctly and prevents regressions."
    },
    7: {
        "title": "Docker Deployment",
        "content": "Containerizing your application makes deployment consistent and reproducible."
    },
    8: {
        "title": "Performance Optimization",
        "content": "Identifying and resolving bottlenecks can dramatically improve user experience."
    },
    9: {
        "title": "Error Handling Strategies",
        "content": "Proper error handling provides better feedback and improves debugging."
    },
    10: {
        "title": "Documentation with FastAPI",
        "content": "FastAPI automatically generates interactive API documentation for your endpoints."
    }
}

# Basic endpoint to get all posts
@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    
    return text_posts

# Endpoint to get a specific post
@app.get("/post/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post

    return new_post
