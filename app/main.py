from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from app.utils.data_loader import load_player_data
from app.utils.nlp_processor import process_natural_language_query

app = FastAPI()

# Load player data when the application starts
player_data = load_player_data("data/player_gamelog_all.csv")

@app.get("/")
def read_root():
    return {"message": "Welcome to the NFL Stats Search API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/players")
def get_all_players():
    if not player_data:
        raise HTTPException(status_code=404, detail="Player data not found")
    return player_data

@app.get("/players/nl_search")
def search_players_natural_language(query: str):
    search_params = process_natural_language_query(query)
    
    results = player_data

    if search_params['min_passing_yards'] is not None:
        results = [player for player in results if player.get('Passing Yds', 0) >= search_params['min_passing_yards']]
    if search_params['min_passing_tds'] is not None:
        results = [player for player in results if player.get('Passing TD', 0) >= search_params['min_passing_tds']]

    if not results:
        raise HTTPException(status_code=404, detail="No players found matching the criteria")

    return results

