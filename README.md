# I. Author's Context
## A. Professional(Non-Technical) Background
I've held leadership roles in numerous VC-backed tech startups, but:
  - they were all __business__ roles (finance, COO, product)
  - I have no CS degree
  - have never undergone a coding bootcamp

## B. Roadmap For 5 Levels of Applied ML Skill Development
### 1. Notebook Toys
- For upskilling and undergrad, not for paid engineering work
- Data is handed to me as a clean and complete CSV download on a silver platter (via Kaggle)
- Analysis is done in a single Jupyter notebook
- Minimal feature engineering

_This was me in 2024_

### 2. Structured Toys
- Maybe interview-ready, but never an employer's best choice
- Introduces data engineering challenges: messy, incomplete, or imbalanced data coming from multiple sources
- Code has been broken down so each file/notebook has a segregated task
- Modeling may go beyond the basics
- Project lives on my laptop i.e. cannot be used by another team member, let alone plugged into a live product

_This is what I'm building towards in 2025, and this project is the first step in the progression from 1 to 2_

### 3. Product That Serves Real World
- A viable candidate for junior roles
- Introduces ML Ops and infrastructure i.e. how will I make a self-contained cardboard box that will be delivered to someone else's address and magically unfold into a big-screen TV without the receiver needing to modify parts or even assemble anything

_This is probably my ceiling given my professional goals, abilities, personality and opportunities_

### 4. Product That Serves Real World At Scale
- Appropriate for senior engineers or getting things done at scale in Big Tech

### 5. Cutting-Edge Research
- Publishing papers or doing pushing the frontiers at some place like OpenAI

# II. What is This?
A level-2 applied Machine Learning project centered around chess.

## A. Burning Questions
### 1. Inflection Point
The chess engine uses a "centipawn evaluation" e.g. if we're at +2.0 White, it means "White is ahead in material and position such that it has 2 extra pawns in a vacuum." I want to know how many points (or pawns) do I need to be before I can say I have an 80% chance of winning?

### 2. Inflection Timing
And in relation to the question above, when does that typically happen? On move #17 in an average game of 40 moves? Is there a moment where the board position is a better predictor of who will win than the players' ELO ratings?

### 3. Minor and Major Piece Development
How predictive is it, if at all, that the person who gets their knights and bishops off the starting spaces for predicting a winner?

Similarly, how good are connected rooks at predicting a winner?

### 4. Castling
Is king-side any different from queen-side castling? Do players who castle have a clear edge over those who don't? And if both players castle, does first player to castle have an edge because of protection and rook activity, or does the second player to castle because of optionality?




## B. Project Components
### 1. Data Retrieval
From the Chess.com API

### 2. Data Storage
Inside a SQLite database

### 3. Data Preparation - Feature Engineering

### 4. Statistical Modeling

### 5. Insights



# III. Major Learnings:
### 1. Data
asdfgasdf