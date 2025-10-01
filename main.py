import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Screen init size:", screen.get_size())

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x, y, PLAYER_RADIUS)

    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    AsteroidField()

    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    while True:

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill("black")
        
        for drawn in drawable:
            drawn.draw(screen)

        updatable.update(dt)
        pygame.display.flip()

        for asteroid in asteroids:
            if asteroid.check_distance(player):
                print('Game over!')
                sys.exit()
            for shot in shots:
                if asteroid.check_distance(shot):
                    asteroid.split()
                    shot.kill()


if __name__ == "__main__":
    main()