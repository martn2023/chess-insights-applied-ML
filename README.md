# I. Author's Context
## A. Professional(Non-Technical) Background
I've held leadership roles in numerous VC-backed tech startups, but:
  - they were all __business__ roles (finance, COO, product)
  - I have no CS degree
  - have never undergone a coding bootcamp

## B. Roadmap For 5 Levels of Applied ML Skill Development
### 1. Notebook Toys
- Appropriate for students, not interview-ready
- Data is handed to me as a clean and complete CSV download on a silver platter (via Kaggle)
- Analysis is done in a single Jupyter notebook
- Minimal feature engineering

### 2. Structured Toys
- Maybe interview-ready, but never an employer's best choice
- Introduces data engineering challenges: messy, incomplete, or imbalanced data coming from multiple sources
- Code has been broken down so each file/notebook has a segregated task
- Modeling may go beyond the basics
- Project lives on my laptop i.e. cannot be used by another team member, let alone plugged into a live product

### 3. Product That Serves Real World
- A viable candidate for junior roles
- Introduces ML Ops and infrastructure i.e. how will I make a self-contained cardboard box that will be delivered to someone else's address and magically unfold into a big-screen TV without the receiver needing to modify parts or even assemble anything

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
**Inflection**: a


### 4. Data Retrieval


- adsf
- adfs



### How to Use
See the 5 Jupyter notebooks to the left

# III. Major Learnings:
#### Data Availability
- It took way longer than I expected to find a suitable data set to work with. There were data sets with mystery titles, had zero documentation on what the feature labels, had too many blank values which nullified their use(no pun intended but seemingly forced), or the row count was too small support a meaningful analysis (particularly dangerous for Stacking)

- Sometimes the data you want isn't all in one source, and maybe it's possible to do a join, but then there's issues where anonymized data (like COVID or financial) prevents you from linking data sets

#### Off-Loading the Heavy Math Responsibilities
- It's astounding how far a novice can go with Scikit-learn doing the heavy lifting on math. Yes, I'm aware a human judgment and domain experience are needed for matters like feature engineering, feature elimination, and explainability. But I can see that you don't need to be a wizard inc college-level Calculus or Stats classes to get the general direction

#### Complaints Over Geron's Level and Other Teaching Materials On Social Media
- This book was recommended to me by someone who likely overestimated my starting point, and it didn't work for me that Geron just jumped right into the material without explaining the taxonomy like I did in my first notebook. I'm committed to finishing this out as a matter of self-discipline, but if I was to advise my younger self, I would have started with something easier before this textbook. Maybe if I 
   mprovements:
#### Sample Data Choices
- If I was to do this again, I would have picked a use case with 100K-500K rows, not 30K.
- I also realize in hindsight that the entire use case, while having some value, is somewhere between a leading and lagging indicator. From a strategic standpoint, I'd want a LEADING indicator. I would want to know who is going to be a deadbeat credit card holder when they apply for the credit card, NOT after +6 months of spending. Or maybe look at a patient profile of healthy people and predict who is going to die of COVID. Or a neat one would be looking at a data on prisoners to see who is likely to re-offend violently if we let them out.
