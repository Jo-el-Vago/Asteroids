import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()
    
    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable, )
    
    Shot.containers = (updatable, drawable, shots)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    game_map = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for obj in asteroids:
            if obj.collision(player1):
                print("Game Over!")
                sys.exit()

        for obj in shots:
            for thing in asteroids:
                if obj.collision(thing):
                    obj.kill()
                    thing.split()
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


        
        
        
        dt = clock.tick(60)/1000

        
        

















if __name__ == "__main__":
    main()
