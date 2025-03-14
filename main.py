import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock =  pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #fills surface with color     
        screen.fill(COLOR_BLACK)

        player.draw(screen)
        player.update(dt)

        # updates displays
        pygame.display.flip()
        # frames per second and calculates delta
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()