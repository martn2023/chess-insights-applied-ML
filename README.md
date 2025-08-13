# I. Author's Context
## A. Professional (Non-Technical) Background
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

**_Entered in 2024, and built up reps in 2025_** :white_check_mark:

### 2. Structured Toys
- Maybe interview-ready, but never an employer's best choice
- Introduces data engineering challenges: messy, incomplete, or imbalanced data, possibly coming from multiple sources
- Code has been broken down so each file/notebook has a segregated task
- Modeling may go beyond the basics
- Cannot be used by another team member, let alone plugged into a live product i.e. it's living on my laptop

**_What I'm transitioning towards in 2025, and this project is the first step in the progression from 1 to 2_** :hourglass_flowing_sand:

### 3. Product That Serves Real World
- A viable candidate for junior roles
- Introduces ML Ops and infrastructure i.e. how will I make a self-contained cardboard box (e.g. Docker) that will be delivered to someone else's address and magically unfold into a big-screen TV without the receiver needing to modify parts or even assemble anything

- **_This is probably my ceiling given my professional goals, abilities, personality and opportunities. I wouldn't creep into this until 2026._** :x:

### 4. Product That Serves Real World At Scale
- Appropriate for senior engineers or getting things done at scale in Big Tech

### 5. Cutting-Edge Research
- Publishing papers or doing pushing the frontiers at some place like OpenAI

# II. What is This?
A level-2 applied Machine Learning project centered around chess.

## A. Burning Questions Inspiring This Project
### 1. Inflection Point
The chess engine uses a "centipawn evaluation" e.g. if we're at +2.0 White, it means "White is ahead in material and position such that it has 2 extra pawns in a vacuum." I want to know how many points (or pawns) do I need to be before I can say I have an 80% chance of winning?

### 2. Inflection Timing
And in relation to the question above, when does that typically happen? On move #17 in an average game of 40 moves? Is there a moment where the board position is a better predictor of who will win than the players' Elo ratings?

### 3. Minor and Major Piece Development
How predictive is it, if at all, that the person who gets their knights and bishops off the starting spaces for predicting a winner?

Similarly, how good are connected rooks at predicting a winner?

### 4. Castling
Is king-side any different from queen-side castling? Do players who castle have a clear edge over those who don't? And if both players castle, does first player to castle have an edge because of protection and rook activity, or does the second player to castle because of optionality?




## B. Project Components and Design
### 1. Data Retrieval
#### a. Chess.com Players' IDs
From the Chess.com API

#### b. Chess Match ID's
From the Chess.com API

#### c. Move History

#### d. Board Position
Evaluated 12 steps deep by Stockfish chess evaluation engine



### 2. Data Storage
Inside a SQLite database

### 3. Data Preparation - Feature Engineering
#### a. On moves
- By piece, with the understanding that castling is a king-oriented move
- By castling
- By piece
#### b. Board States
- 4 minors off their start squares
- rooks achieve connection connected
- castling status

### 4. Statistical Modeling

### 5. Insights

# III. Tradeoffs and Rationale
## A. SQLite vs. Postgres
### 1. Arguments for SQLite
- Self-contained in a single file, which is portable i.e. I can move it to a public GitHub repo without worrying about transferring environment variables via Docker
- Skips role management setup and credential management for people who don't exist

### 2. Arguments for Postgres
- Avoids the performance issues of having a single file open to 1 user for 1 process at time (concurrency)
- Has more sophisticated user management abilities
- Better scalability potential if the data size surpasses 

Postgres' advantages are only relevant when there's multiple consumers attacking this or multiple team members working on this at once. While I'm eager to level up my engineering skills, picking Postgres for **this project feels like "Engineering Theater"**.

# IV. Major Learnings
## A. Notation For Board Positions
The code uses "FEN", which is "Forsyth–Edwards Notation" for chess positions. I thought maybe the computer would use a matrix to show an 8x8 grid and then tack on a binary marker for whose turn it is. There has to be something that tracks en-passant eligibility, castling status/rights https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation





# V. Quick-Start Guide

