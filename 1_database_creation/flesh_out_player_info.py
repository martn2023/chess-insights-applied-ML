import sqlite3
import requests
import time
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path = os.path.join(project_root, "chess_insights.sqlite")
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("SELECT username FROM players")
usernames = [row[0] for row in cursor.fetchall()]

def fetch_profile(username):
    url = f"https://api.chess.com/pub/player/{username}"
    headers = {
        "User-Agent": "chess-insights-bot"
    }
    print("we trying url:", url)
    try:
        response = requests.get(url, headers = headers)
        #print(response)
        if response.status_code == 200:
            data = response.json()
            print("data time", data)
            return {
                "uuid": data.get("player_id"),
                "title": data.get("title")
            }
        else:
            print(f"❌ {username} returned status {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error fetching {username}: {e}")
        return None


counter = 0
# Main loop
for i, username in enumerate(usernames):
    counter += 1
    if counter > 5:
        break

    profile = fetch_profile(username)
    if profile:
        try:
            cursor.execute(
                "UPDATE players SET uuid = ?, title = ? WHERE username = ?",
                (profile["uuid"], profile["title"], username)
            )
        except Exception as e:
            print(f"❌ Error inserting for {username}: {e}")

    # Respect API rate limit
    time.sleep(0)

    # Optional: feedback every 100
    if i % 10 == 0:
        print(f"✅ Processed {i} players...")

# Commit once at the end
conn.commit()
conn.close()

print("✅ Done updating player profiles.")
