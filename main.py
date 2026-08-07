from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Or specify your frontend URL
    allow_credentials=False,  # Use False with "*"
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/items")
def get_user_profile():
    return {
        "id": 101,
        "username": "aliixdev",
        "is_admin": True,
        "skills": ["Python", "JavaScript", "HTML"]
    }
