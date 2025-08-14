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
**Placeholder**, as the analysis can only come after data is processed
### 5. Insights
**Placeholder**, as the insights can only come after a formal and varied analysis

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

## B. Whether to Pre-Compute Derived Fields in "Matches" Database Table
The first example would be calculating the name of a match winner.

### 1. Arguments for Pre-Computing
- Easier to do analysis later, because you can search for games by winner instead of having to  write clunky code that checks the results of both white and black and then checks the names of both players, and then filters without regards to color
- UUID will never change, and Username is unlikely to change, and it won't be a problem since this analysis is non-recurring
- Table complexity isn't yet an issue because the number of dimensions initially pulled is ~15 and even ~5 engineered features would put the count at 20 columns, still manageable mentally and readable on a monitor
- Data storage won't matter because we're talking 10MB-100MB, not even 1GB

### 2. Arguments for Minimalist Approach In Table Design
- Technically, a username could change, so you'd be relying on mutable data
- Someone might argue this is redundant because it could 100% be calculated with known fields later on in different analysis.
- From a signaling and credibility standpoint, this is the "safer" route because experienced engineers generally try to avoid pre-computing until proven necessary (runtime fears)

I went for the pre-computing route in the interest of expediency

# IV. Major Learnings
## A. Notation For Board Positions
The code uses "FEN", which is "Forsyth–Edwards Notation" for chess positions. I thought maybe the computer would use a matrix to show an 8x8 grid and then tack on a binary marker for whose turn it is. There has to be something that tracks en-passant eligibility, castling status/rights https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation

## B. Using Three Data Structures At Once for BFS
When I was populating the table of plaeyrs, I wanted to plant 5 seeds and gain diversity through a BFS, not DFS. Outside of LeetCode this was my first Breadth-First Search. If I used a queue (FIFO), I could get the ordering I wanted for which players to search, but every time I ran into a duplicate name, I'd have to search the whole queue again to avoid double-touching. I then considered using a stack, which would have faster lookups, but wouldn't have the ordering I needed. What I hadn't considered until this project was using BOTH at the same time. What I ended up doing was having 3 parts:
- Queue to manage BFS (FIFO)
- 1st Set to manage opponents I had come across
- 2nd Set to manage opponents I had already provided details about to our database


## C. API Pulls May Require Headers
I was blocked on one of my data pull scripts until I put a header in

## D. Teachable Moment About Not Segregating Out A Function That Looks Up Player Profile Details
I made a rookie mistake of having one consolidated function that looks up a player's opponent history and then logs those names into a "players" database table. My strategy was to build the list of players first, then pull a handful of games from each player.

This was fundamentally incomplete because I forgot that there would be situations later where I would run into opponent usernames I had never encountered/recorded in the "players" table. Without a corresponding player record, we couldn't do foreign keys in the "matches" table.

I could have backpedaled and have rewritten this, to appear less chaotic. In the interest of keeping momentum and practicing iterative triage work seen in real life, I elected a Band-Aid strategy: record the names of players in the **matches** table without a foreign key, then write a corrective script to fill out the missing player details in the **players* table after the match data has been pulled.

## E. Dangers of Using SQLite
My logic was that SQLite was low-risk because the file size would be small, not realizing that it can still be vulnerable during interrupted state transitions. But why would I expect that for such a low level of required processing power and memory, right? As if fate wanted to teach me a lesson, the system crashed and corrupted my database and I was only able to save 8 hours of API retrievals by pulling a fresh backup from GitHub.
  

# V. Quick-Start Guide
- Clone onto your device
- pip install -r requirements.txt, to install libraries
- Run the scripts in the 1_database_creation folder to
    - initialize an empty database
    - create the players table
    - create the matches table
    - create the moves table
- Pick your own seeds in seed_players