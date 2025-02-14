import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	bullets = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Bullet.containers = (updatable, drawable, bullets)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for obj in updatable:
			obj.update(dt)

		screen.fill("black")
		
		for asteroid in asteroids:
			if asteroid.detect_collision(player):
				print("Game over!")
				exit()
			for bullet in bullets:
				if asteroid.detect_collision(bullet):
					asteroid.split()
					bullet.kill()

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		# limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
