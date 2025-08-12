# data_ingestion/get_games_july2025.py

import requests
import json

username = "magnuscarlsen"
month_url = f"https://api.chess.com/pub/player/{username}/games/2025/07"
headers = {"User-Agent": "chess-insights-dev"}

resp = requests.get(month_url, headers=headers)

if resp.status_code == 200:
    data = resp.json()
    games = data.get("games", [])

    # Save raw output
    with open(f"{username}_games_2025_07.json", "w") as f:
        json.dump(games, f, indent=2)

    print(f"✅ Saved {len(games)} games for {username} in July 2025.")
else:
    print(f"❌ Error {resp.status_code}: {resp.text}")
