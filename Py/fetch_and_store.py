import requests
import json

def fetch_games():
    """Fetches game data from the API and returns a list of dictionaries."""
    url = f"https://www.freetogame.com/api/games"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json()

def save_games_to_json(games, filename="games.json"):
    """Saves the game data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(games, f, indent=4)

if __name__ == "__main__":
    games = fetch_games()  # You can specify other platforms here
    save_games_to_json(games) 
    print("Game data fetched and saved to 'games.json'")