from fastapi import FastAPI, HTTPException
from app.utils.data_loader import load_player_data

# Create a FastAPI instance
app = FastAPI()

# Load player data when the application starts
player_data = load_player_data("data/player_gamelog_all.csv")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the NFL Stats Search API"}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Endpoint to get all player data
@app.get("/players")
def get_all_players():
    if not player_data:
        raise HTTPException(status_code=404, detail="Player data not found")
    return player_data
