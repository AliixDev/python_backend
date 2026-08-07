from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CRITICAL: This allows your GitHub Pages UI to connect safely without security blocks
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def read_root():
    return {"message": "Api Ok "}
    @app.get("/api/items")
def get_products():
    return ["Laptop", "Mouse", "Keyboard", "Monitor"]

