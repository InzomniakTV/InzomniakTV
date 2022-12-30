import pygame

# Initialize Pygame
pygame.init()

# Set the window size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the title of the window
pygame.display.set_caption('Pong')

# Set the initial positions of the paddles
paddle1_pos = [20, screen_height // 2]
paddle2_pos = [screen_width - 20, screen_height // 2]

# Set the initial positions of the ball
ball_pos = [screen_width // 2, screen_height // 2]

# Set the initial velocities of the ball
ball_vel = [2, 2]

# Set the initial score
score1 = 0
score2 = 0

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the positions of the paddles and the ball
    paddle1_pos[1] += 2
    paddle2_pos[1] += 2
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Check if the ball is off the screen
    if ball_pos[0] > screen_width or ball_pos[0] < 0:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] > screen_height or ball_pos[1] < 0:
        ball_vel[1] = -ball_vel[1]

    # Check if the ball hits a paddle
    if ball_pos[0] <= 20 and abs(ball_pos[1] - paddle1_pos[1]) < 50:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[0] >= screen_width - 20 and abs(ball_pos[1] - paddle2_pos[1]) < 50:
        ball_vel[0] = -ball_vel[0]

    # Check if a player scored
    if ball_pos[0] <= 0:
        score2 += 1
        ball_pos = [screen_width // 2, screen_height // 2]
    if ball_pos[0] >= screen_width:
        score1 += 1
        ball_pos = [screen_width // 2, screen_height // 2]

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the paddles and the ball
    pygame.draw.rect(screen, (255, 255, 255), (paddle1_pos[0], paddle1_pos[1] - 50, 10, 100))
    pygame.draw.rect(screen, (255, 255, 255), (paddle2_pos[0], paddle2_pos[1] - 50, 10, 100))
    pygame.draw.rect(screen, (255, 255, 255), (ball_pos[0] - 5, ball_pos[1] - 5, 10, 10))

