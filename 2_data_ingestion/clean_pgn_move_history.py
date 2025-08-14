import re
import chess.pgn
from io import StringIO

def clean_pgn(raw_pgn: str) -> str:
    """
    Removes PGN headers and in-move clock annotations.
    Returns a flat, clean move string ready for FEN generation.
    """
    # Remove PGN header lines
    move_lines = [line for line in raw_pgn.splitlines() if not line.startswith("[")]
    move_body = "\n".join(move_lines)

    # Remove annotations like {[%clk 0:02:55.4]}
    no_annotations = re.sub(r"\{[^}]*\}", "", move_body)

    # Normalize whitespace
    cleaned_pgn = re.sub(r"\s+", " ", no_annotations).strip()

    return cleaned_pgn

def pgn_to_fens(pgn_str: str) -> list:
    """
    Converts a cleaned PGN string into a list of tuples:
    (move_number, color, FEN)
    """
    game = chess.pgn.read_game(StringIO(pgn_str))
    board = game.board()

    result = []
    move_number = 1

    for idx, move in enumerate(game.mainline_moves()):
        board.push(move)
        color = "white" if idx % 2 == 0 else "black"
        fen = board.fen()
        result.append((move_number, color, fen))
        if color == "black":
            move_number += 1

    return result
