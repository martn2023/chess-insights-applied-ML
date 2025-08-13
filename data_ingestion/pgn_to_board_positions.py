import re
import chess.pgn
from io import StringIO

def clean_pgn(raw_pgn: str) -> str:
    """
    Removes annotations (clock times, comments) from PGN string.
    Keeps all headers and moves intact.
    """
    no_comments = re.sub(r"\{[^}]*\}", "", raw_pgn)
    clean_lines = [line.strip() for line in no_comments.splitlines()]
    return "\n".join(clean_lines)

def pgn_to_fens(pgn_str: str) -> list:
    """
    Converts PGN string into a list of (move_number, FEN) tuples.
    """
    game = chess.pgn.read_game(StringIO(pgn_str))
    board = game.board()
    fens = []
    move_number = 1
    for move in game.mainline_moves():
        board.push(move)
        fens.append((move_number, board.fen()))
        move_number += 1
    return fens

# --- Example usage starting from JSON ---
# Pretend this is the Chess.com API response (Python dict after json.loads)
sample_game_json = {
    "pgn": "[Event \"Live Chess\"]\n[Site \"Chess.com\"]\n[Date \"2025.07.01\"]\n[Round \"-\"]\n"
           "[White \"MagnusCarlsen\"]\n[Black \"KnightOclock\"]\n[Result \"1-0\"]\n"
           "1. d4 {[%clk 0:02:55.4]} 1... Nf6 {[%clk 0:02:58.5]} 2. c3 {[%clk 0:02:56.2]}\n"
}

#this is still too dirty for chess engine to interpret because it has timestamps and funny use of periods to denote which player to act
pgn_with_time_stamps = sample_game_json["pgn"]

cleaned_pgn = clean_pgn(pgn_with_time_stamps)

fens_positions_list = pgn_to_fens(cleaned_pgn)

print("First 3 FENs:")
for move, fen in fens_positions_list[:3]:
    print(f"Move {move}: {fen}")
