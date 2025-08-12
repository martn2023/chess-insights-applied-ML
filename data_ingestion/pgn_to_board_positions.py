# parse_pgn_positions.py

import json
import chess.pgn

# Input & Output paths
INPUT_JSON = "magnuscarlsen_games_2025_07.json"

# Load the games JSON (already pulled from Chess.com)
with open(INPUT_JSON, "r") as f:
    games = json.load(f)

for game in games:
    pgn_text = game.get("pgn")
    if not pgn_text:
        continue

    # Use python-chess PGN parser
    pgn_io = chess.pgn.read_game(io.StringIO(pgn_text))

    # Start from initial board
    board = pgn_io.board()

    print(f"Game: {game['url']}")
    for move_num, move in enumerate(pgn_io.mainline_moves(), start=1):
        board.push(move)
        print(f"Move {move_num}: {board.san(move)}")
        print(board)  # ASCII board representation
