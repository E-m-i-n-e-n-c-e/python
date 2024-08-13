import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

# Player attributes
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10
player_speed = 5

# Bullet attributes
bullet_image = pygame.Surface((10, 20))
bullet_image.fill(RED)
bullet_rect = bullet_image.get_rect()
bullet_speed = 10
bullets = []

# Target attributes
target_image = pygame.Surface((40, 40))
target_image.fill(RED)
targets = [pygame.Rect(random.randint(0, WIDTH - 40), random.randint(50, 400), 40, 40) for _ in range(5)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    # Shooting
    if keys[pygame.K_SPACE]:
        bullet_rect = bullet_image.get_rect()
        bullet_rect.centerx = player_rect.centerx
        bullet_rect.centery = player_rect.top
        bullets.append(bullet_rect)

    # Update bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Check for collisions
    for bullet in bullets:
        for target in targets:
            if bullet.colliderect(target):
                bullets.remove(bullet)
                targets.remove(target)

    # Draw everything
    screen.fill(WHITE)
    screen.blit(player_image, player_rect)
    for target in targets:
        screen.blit(target_image, target)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    pygame.display.flip()

# Quit the game
pygame.quit()