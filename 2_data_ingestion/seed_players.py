from get_montly_game_history_by_username import fetch_games_for_month
import sqlite3
import os

# SQLite db file should NOT be in this folder, should be one level up in the root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(project_root, "chess_insights.sqlite")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

#I wanted to plant random 5 seeds at different Elo levels and watch them spread out via BFS
seed_players_list = [

    "SvAlpha", #800s
    "Yashk05", #2000s
    "magnuscarlsen" #3300s
]

archive_year = 2025
archive_month = 7

initial_pull_per_seed = 50000 # this is how I got 50,008 records

from collections import deque

def bfs_player_crawl(seed_players, year, month, max_players):
    players_seen_set = set()
    players_processed_set = set()
    queue = deque(seed_players) #forming my FIFO line, not using an array
    #print("initial que", queue)

    while len(players_processed_set) < max_players:
        current_player = queue.popleft().lower()
        #print("current_player", current_player)
        if current_player in players_processed_set:
            continue

        players_seen_set.add(current_player)

        games = fetch_games_for_month(current_player, year, month)
        if games is None:
            print(f"❌ Skipping {current_player} — invalid username???")
            continue
        else:
            #print("archives found for:", current_player)
            pass
        players_processed_set.add(current_player)

        opponents_set = set()
        for game in games:
            w = game.get("white", {}).get("username", "").lower()
            b = game.get("black", {}).get("username", "").lower()
            if w and b:
                opponents_set.add(b if w == current_player else w)

        #print("opponents_set found", opponents_set)
        # add someone in back of the queue
        for opp in opponents_set:
            if opp not in players_seen_set:
                queue.append(opp)
                players_seen_set.add(opp)

        #print("queue with new opponents added", queue)
        if len(players_seen_set) >= max_players:
            #print("capacity reached")
            print("players_seen_set reached", players_seen_set, len(players_seen_set))
            #print("queue reached", queue)
            break

    print(f"🌍 Finished crawl: {len(players_seen_set)} unique players collected.")
    #print(players_seen_set)
    return players_seen_set

make_players = bfs_player_crawl(seed_players_list, archive_year, archive_month, initial_pull_per_seed)



for username in make_players:
    try:
        cursor.execute("INSERT OR IGNORE INTO players (username) VALUES (?)", (username,))
    except Exception as e:
        print(f"Error inserting {username}: {e}")

conn.commit()
conn.close()

print("✅ All players inserted into 'players' table.")