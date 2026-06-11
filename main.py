from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI application
app = FastAPI(title="Landscape VS Code Extension Backend")

# MANDATORY: Enable CORS so your VS Code extension can talk to this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows connections from VS Code
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE
    allow_headers=["*"],  # Allows all headers
)

# Root endpoint to quickly verify the server is alive
@app.get("/")
def read_root():
    return {"status": "online", "message": "Landscape server is running!"}

# Common health check or initialization endpoint extensions look for
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# A placeholder POST endpoint in case your extension sends data
@app.post("/api/landscape")
def receive_data(payload: dict):
    print(f"Received data from VS Code: {payload}")
    return {"status": "success", "received": payload}

# This section allows you to run the script directly with Python
if __name__ == "__main__":
    import uvicorn
    # Runs the server on localhost:8000 with auto-reload enabled
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
