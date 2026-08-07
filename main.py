from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/items")
def get_products():
    return ["Laptop", "Mouse", "Keyboard", "Monitor"]

@app.get("/profile")
def get_user_profile():
    return {
        "id": 101,
        "username": "aliixdev",
        "is_admin": True,
        "skills": ["Python", "JavaScript", "HTML"]
    }
