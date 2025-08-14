import sqlite3
import os
from itertools import count

from get_monthly_game_history_by_username import fetch_games_for_month
from clean_pgn_move_history import clean_pgn, pgn_to_fens


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(project_root, "chess_insights.sqlite")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

#this is coming from SQLite db, not from API calls anymore
def get_all_players():
    cursor.execute("SELECT username FROM players")
    rows = cursor.fetchall() #tuples,not a clean list yet
    usernames_list = []
    for row in rows:
        usernames_list.append(row[0])
    #print(usernames_list[:10])
    return usernames_list

usernames_list = get_all_players()

def populate_some_matches(usernames_list):
    countdown = len(usernames_list)
    for username in usernames_list:
        monthly_match_archive = fetch_games_for_month(username, 2025, 7) #Aware this is a "magic number" but keeping it simple
        if not monthly_match_archive: # we shouldn't need this error catching because in my use case, I only pulled for 1 month of games
            continue

        for individual_match_info in monthly_match_archive[:3]: # capped at 3, but will still work if less than 3 entries
            #print("indiv match info", individual_match_info)
            # start matching shit 1 to 1 with the database



            # Step 1: Extract fields from JSON
            game_id = individual_match_info["uuid"]
            url = individual_match_info["url"]
            time_control = individual_match_info["time_control"]
            timing_class = individual_match_info["time_class"]

            # Winner
            white_result = individual_match_info["white"]["result"]
            black_result = individual_match_info["black"]["result"]
            if white_result == "win":
                winner_uuid = individual_match_info["white"]["uuid"]
                winner_username = individual_match_info["white"]["username"]
            elif black_result == "win":
                winner_uuid = individual_match_info["black"]["uuid"]
                winner_username = individual_match_info["black"]["username"]
            else:
                winner_uuid = None
                winner_username = None

            # Raw PGN
            raw_pgn = individual_match_info["pgn"]

            # White info
            white_username = individual_match_info["white"]["username"]
            white_elo_rating = individual_match_info["white"]["rating"]
            white_opening = individual_match_info.get("eco", None)
            white_accuracy = None  # Not provided by archive API
            white_result = individual_match_info["white"]["result"]

            # Black info
            black_username = individual_match_info["black"]["username"]
            black_elo_rating = individual_match_info["black"]["rating"]
            black_opening = individual_match_info.get("eco", None)
            black_accuracy = None  # Not provided by archive API
            black_result = individual_match_info["black"]["result"]

            # Step 2: Insert into matches table (without cleaned PGN for now)
            cursor.execute("""
                           INSERT OR IGNORE INTO matches (
                               game_id,
                               url,
                               time_control,
                               timing_class,
                               winner_uuid,
                               winner_username,
                               raw_pgn,
                               clean_pgn,

                               white_username,
                               white_elo_rating,
                               white_opening,
                               white_accuracy,
                               white_result,

                               black_username,
                               black_elo_rating,
                               black_opening,
                               black_accuracy,
                               black_result
                           ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                       """, (
                game_id,
                url,
                time_control,
                timing_class,
                winner_uuid,
                winner_username,
                raw_pgn,
                None,  # leave cleaned_pgn blank for now

                white_username,
                white_elo_rating,
                white_opening,
                white_accuracy,
                white_result,

                black_username,
                black_elo_rating,
                black_opening,
                black_accuracy,
                black_result
            ))

            #print(f"✅ Inserted game {game_id}, everything but the cleaned PGN")

            # summon the function to clean the pgn before inserting it into the db
            cleaned_pgn = clean_pgn(individual_match_info["pgn"])
            #print("prove cleaned pgn", cleaned_pgn)

            cursor.execute("""
                    UPDATE matches
                    SET clean_pgn = ?
                    WHERE game_id = ?
                """, (cleaned_pgn, game_id))

        if countdown % 1000 == 0:
            conn.commit()
            print(f"committed {countdown} remaining")
            # hesitant to place this outside of the loop because I wanted to save after every row, but compromised to do every 1000 rows in a 50K run

        countdown -= 1
        #print("usernames remaining", countdown)

        #print("first match", monthly_match_archive[0])
        # temporary breakage to avoid overkill during testing


result = populate_some_matches(usernames_list)