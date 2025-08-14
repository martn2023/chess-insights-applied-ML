import sqlite3
import os
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
    print(usernames_list[:10])
    return usernames_list

usernames_list = get_all_players()

def populate_some_matches(usernames_list):
    for username in usernames_list:
        monthly_match_archive = fetch_games_for_month(username, 2025, 7) #Aware this is a "magic number" but keeping it simple
        if not monthly_match_archive: # we shouldn't need this error catching because in my use case, I only pulled for 1 month of games
            continue

        for individual_match_info in monthly_match_archive[:3]: # capped at 3, but will still work if less than 3 entries
            print("indiv match info", individual_match_info)
            # start matching shit 1 to 1 with the database
            # summon the function to clean the pgn before inserting it into the db
            cleaned_pgn = clean_pgn(individual_match_info["pgn"])
            print("prove cleaned pgn", cleaned_pgn)



        #print("first match", monthly_match_archive[0])
        break # temporary breakage to avoid overkill during testing


result = populate_some_matches(usernames_list)