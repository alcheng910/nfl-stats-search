from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the NFL Stats Search API"}

# Define a simple health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}
