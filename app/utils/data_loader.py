import pandas as pd

def load_player_data(csv_path: str):
    try:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(csv_path)
        
        # Handle out of range float values: replace NaNs and infinite values
        data = data.fillna(0)  # Replace NaN with 0
        data = data.replace([float('inf'), float('-inf')], 0)  # Replace infinite values with 0
        
        # Convert DataFrame to a list of dictionaries (JSON-like)
        return data.to_dict(orient='records')
    except Exception as e:
        print(f"Error loading player data: {e}")
        return []
