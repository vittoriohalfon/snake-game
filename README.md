# SNAKE GAME

# Pygame Snake Game
This script is a simple implementation of the classic Snake game using the Pygame library. The player controls a snake, moving it around the screen to eat food while avoiding hitting the walls or itself.

## Requirements
- Python3
- Pygame

## Installation
Before you can run the game, you need to install Pygame. You can install it via pip:

bash
pip install pygame

## How to Play
Run the script to start the game.
Use the arrow keys (←, ↑, →, ↓) to control the direction of the snake.
Eat the red blocks (food) that appear randomly on the screen to grow the snake in length.
Avoid running into the walls or the snake's own body.

## Features
Window Settings: The game window is set to 640x480 pixels.
Game Mechanics: The snake moves in a grid, and the player tries to eat food to increase the length of the snake.
Score Display: The current score, representing the length of the snake minus one, is displayed in the top-left corner.
Game Over Conditions: The game ends if the snake hits the wall or itself.
Restart Option: Upon game over, the player can choose to quit or restart the game.

## Code Structure
- Initialization: Pygame is initialized, and game settings such as window dimensions, colors, and font are set.
- Game Functions:
    - display_score(score): Displays the current score.
    - draw_snake(block_size, snake_List): Draws the snake on the screen.
    - gameLoop(): Contains the main game loop which handles game logic, rendering, and user input.

## Ending the Game
To quit the game, close the game window or press 'Q' when the game over message is displayed. To play again after losing, press 'C'.
