# BrickBreaker-PROJECT

# Press Space and Start Playing!!
`Brick Breaker` is a classic arcade game where players control a paddle to bounce a ball and break bricks on the screen. The objective is to clear all the bricks without letting the ball fall off the bottom.

## Game Mechanics
- Press space to start the game 
- The player controls a paddle using keyboard user input to move the paddle horizntally- left key for left and right key for right
- The ball starts from the middle to project downwards in any direction, and the user has to bounce it back to hit the bricks above
- Bricks break(disappear) once the ball touches it
- Speed of the ball is incremented with passing of time making it challenging
- The game ends when either:
    - The player breaks all the bricks before using up all 3lives, resulting in their `Victory`
    - Or if the user fails to hit the ball before it touches the ground 3 times in a row resulting in `Gameover`

## Walkthrough On Running The Game
The various elements of the game are divided into 2 Sections:

## 1. Python code files
- `BrickBreaker.py`: This is the main game file which incoorporates the other file content to include in the game adding to functionality and visuals

To run the files, set up the python virtual environment:
### Activating the Virtual Environment

To activate the virtual environment for this project, follow these steps based on your operating system:

### Windows
``` bash
.\venv\Scripts\activate
```

### macOS/Linux
``` bash
source venv\Scripts\activate
```
Once activated, you should see (venv) appear in your terminal, indicating the virtual environment is active.

To run the BrickBreaker.py file now use the command:
``` bash
python3 BrickBreaker.py
```
This will open a pygame window that runs the game smoothly.

- `ball.py` is the python file associated with the attributes and functions related to the working of the ball. 

- `brick.py` is the python file which is associated with setting the various styling and function of the multiple array of bricks present in the game

- `paddle.py` is the file that takes care of the same for the functioning of paddle

## 2. Media Files
- `background.jpg` sets the background of the game window
- `brass-fanfare-with-timpani-and-winchimes-reverberated-146260.mp3` is the victory music played when the player wins the game by breaking all the breaks
- `brick-dropped-on-other-bricks-14722.mp3` is the sound played when the bricks come in contact with the ball
- `fail-144746.mp3` is used when the ball falls below the line resulting in player losinig a life
- `game-over-arcade-6435.mp3` is played when the player loses all three lives and this leads to game over that resets the game
- `tennis-ball-hit-151257.mp3` is played when the ball comes in contact with the paddle

## Conclusion 
In short, this game was intended to be made to understand the general requirements and techniques regarding creating and developing a simple game for beginners using pygame.<br>

Since there is an absence of instruction regarding documenting the whole experience of making the game, I'm only providing the important details and guidance regarding running the program, in hopes of my efforts being sufficient.<br>

Thank you for taking the time to explore my project repository! I truly appreciate your interest and hope you find it as enjoyable and valuable as I did while creating it.









