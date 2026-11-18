import pygame
import time

pygame.display.set_caption("Badüdüd Clicker")
clock = pygame.time.Clock

# Setting game window dimensions

game_display = pygame.display.set_mode((540,674))
# Loading the image
bg_image = pygame.image.load('background.png')
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Drawing image at position (0,0)
    game_display.blit(bg_image, (0, 0))
    pygame.display.update()
pygame.quit()







while True:
    clock.tick(60)
    screen.fill((9,0,0))
    screen.blit(bg,(0,0))
    x,y = pygame.mouse.get_pos()
    screen.blit(bg, (0, 0))


time.sleep(10)
pygame.quit()