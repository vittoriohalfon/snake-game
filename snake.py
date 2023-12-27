import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

# Set the game clock
clock = pygame.time.Clock()

# Set the font for the score
font = pygame.font.SysFont(None, 25)

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the snake block size and speed
block_size = 10
snake_speed = 15

# Define the function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, [0, 0])

# Define the function to draw the snake
def draw_snake(block_size, snake_List):
    for x in snake_List:
        pygame.draw.rect(window, black, [x[0], x[1], block_size, block_size])

# Define the main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Set the initial position and direction of the snake
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0

    # Create the initial snake
    snake_List = []
    Length_of_snake = 1

    # Set the initial position of the food
    foodx = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0

    while not game_over:

        # Display a message when the game is over
        while game_close == True:
            window.fill(black)
            message = font.render("Game Over! Press Q-Quit or C-Play Again", True, white)
            window.blit(message, [window_width / 6, window_height / 3])
            display_score(Length_of_snake - 1)
            pygame.display.update()

            # Wait for the player to choose to quit or play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Move the snake based on the arrow key pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check if the snake hits the wall
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change

        # Draw the background
        window.fill(black)

        # Draw the food
        pygame.draw.rect(window, red, [foodx, foody, block_size, block_size])

        # Update the snake's position
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if (len(snake_List) > Length_of_snake):
            del snake_List[0]
        
        # Check if the snake hits itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        # Draw the snake
        draw_snake(block_size, snake_List)

        # Display the score
        display_score(Length_of_snake - 1)

        #Update the window
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
            Length_of_snake += 1

        # Set the game speed
        clock.tick(snake_speed)

        # Quit the game
    pygame.quit()
    quit()

gameLoop()
        