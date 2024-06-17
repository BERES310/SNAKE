Description
This Python program implements a classic Snake game using the Pygame library. The game offers single-player and multiplayer modes (local multiplayer on the same screen).

Features
Single Player Mode: Control a snake to eat food and grow longer. Avoid collisions with walls and yourself.
Multiplayer Mode (Type 4): Two players control separate snakes simultaneously using different sets of keys.
Scoreboard: Tracks scores for both players in multiplayer mode.
Walls and Obstacles: May include walls that the snakes cannot pass through, depending on the game mode.
Sound Effects: Includes background music, eating sound effects, and game over sounds.
Dynamic Food: Different types of food with varying effects on scores and snake growth.
Game Over Handling: Allows players to continue or quit the game after losing.


Components:
snake.py: Defines the Snake class and its movement methods.
food.py: Manages different types of food items.
scoreboard.py: Handles scoring and displaying scores on the screen.
wall.py: Implements walls or obstacles in the game.
GameSettings.py: Contains game settings like screen dimensions, speed, and game type.
timer.py: Controls the game timer displayed on the screen.



Dependencies:
Python 3.x
Pygame library (pygame)


Installation:
Ensure Python and Pygame are installed.
Clone the repository or download the source code.


Running the Game:
Execute the snake_game.py script.
Use the arrow keys (Player 1) or WASD keys (Player 1) for movement.
For multiplayer mode (Type 4), additional keys are used for Player 2.


Game Controls:
    Single Player:
    Arrow keys: Up, Down, Left, Right for movement.

    Multiplayer (Type 4):
    Player 1 (Snake 1): Arrow keys for movement.
    Player 2 (Snake 2): WASD keys for movement.


Game Rules
Objective: Eat food items to grow longer and increase your score.
Collision: Avoid colliding with walls, obstacles, or your own snake's body segments.
Game Over: The game ends when a snake collides with a wall, obstacle, or itself. Players can choose to continue or quit.


Notes
The game includes features such as dynamic food generation, scoring mechanics, and sound effects to enhance the gaming experience.
Players can adjust game settings like speed and game type through GameSettings.py.
Score data is stored locally in score.txt and updated based on the highest score achieved.
Contributions
Contributions and improvements to the game are welcome through pull requests.
For major changes, please open an issue first to discuss potential improvements.




Credits
Developed by Jan Beres.
Built using Python and Pygame.