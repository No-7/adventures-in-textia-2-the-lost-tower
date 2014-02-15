import pygame
import datetime

window_width = int(input("Window Width"))
window_height = int(input("Window Height"))

screen = pygame.display.set_mode((window_width, window_height))
running = 1

# red = int(input("Red?"))
# green = int(input("Green?"))
# blue = int(input("Blue?"))


while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	#screen.fill((red, green, blue))
	screen.fill((100, 100, 100))
	pygame.draw.aaline(screen, (0, 0, 255), (639, 0), (0, 479))
	pygame.draw.line(screen, (0, 0, 255), (0, 0), (639, 479))
	pygame.display.flip()
