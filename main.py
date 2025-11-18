import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid




def main():
    print(f"Starting Asteroids with Pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock(); dt = 0 #creates a clock class item with dt(delta-time) counter

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000 # this logs the time between screen refreshes
        
        updatable.update(dt)

        screen.fill("black")
        
        for chr in drawable:
            chr.draw(screen)
            
        pygame.display.flip()   # this gives us a refresh on the screen
        
        dt = clock.tick(60) / 1000 # this logs the time between screen refreshes


if __name__ == "__main__":
    main()
