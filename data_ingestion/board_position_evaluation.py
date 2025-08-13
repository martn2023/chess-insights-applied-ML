from stockfish import Stockfish

stockfish = Stockfish(path="../engines/stockfish/stockfish-windows-x86-64-avx2.exe")

# Sample board position (from your earlier game)
fen = "q25/p2n4/1p3k2/8/2KP1BR1/2P5/PP6/8 b - - 0 45"

fen2 = "rnbqkb1r/pppppppp/5n2/8/3P4/2P5/PP2PPPP/RNBQKBNR b KQkq - 0 2"




# Set the position
stockfish.set_fen_position(fen2)

# Get evaluation
evaluation = stockfish.get_evaluation()

print("📌 Evaluation:", evaluation)
