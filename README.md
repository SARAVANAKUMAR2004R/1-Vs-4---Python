Turn-Based Number Smash Game

Introduction:

        This is a turn-based elimination game where 5 players (A, B, C, D, and E) compete to outlast one another. Each player starts with 5 lives, and their goal is to avoid losing lives while causing other players to lose theirs by selecting numbers strategically. Player A is controlled by the user, while players B, C, D, and E are controlled by the computer.

Game Mechanics:

    The game runs on Python, with each player starting the game with 5 lives.

    The game progresses through rounds where each player chooses a number between 1 and 5.

    The player who picks the highest number in each round loses one life.
    
Win/Loss Conditions:

    The game continues until all but one player has lost all their lives.
    
    If player A (the user) loses all lives, they lose the game.
    
    If player A outlasts all other players, they win the game.
    
Features:

    Random number generation for computer-controlled players (B, C, D, and E).
    
    Each player can only pick numbers that have not been chosen in that round.
    
    Players are eliminated when they lose all their lives.

    Special conditions affect player A’s survival if they haven’t lost lives after a certain number of rounds.

Rules:

    Choosing a Number: Each round, player A (user) selects a number between 1 and 5. Other players (B, C, D, E) randomly select their numbers.
    
    Avoid Duplicates: Players cannot select a number that has already been chosen during the current round.
    
    Losing a Life: At the end of each round, the player who selected the highest number loses a life.
    
    Special Conditions: If player A has too many lives after a certain number of rounds, they lose a life to keep the game balanced.
    
How to Run the Game:

    Clone or download this repository.
    
    Ensure you have Python installed (at least version 3.6+).
    
    Install any necessary dependencies (e.g., the emoji library if you're using emojis).
    
bash:

    pip install emoji
    
Run the game in the terminal:

bash:

    python <file name>.py



