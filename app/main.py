# Task 2 - Abdullah Salih

from fastapi import FastAPI
from routes import user_routes, post_routes
from dependencies.database import Tortoise, init_tortoise

app = FastAPI()

# Include routes from the routes folder
app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(post_routes.router, prefix="/posts", tags=["posts"])

# Initialize Tortoise ORM
init_tortoise(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
