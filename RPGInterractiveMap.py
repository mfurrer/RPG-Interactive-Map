
## InteractiveMap
##
## 2015-01-10 ## initial version


import sys, pygame, random

def main():
	pygame.init()
	size = width, height = 640,480
	screen = pygame.display.set_mode(size)
	balls = []
	pygame.display.set_caption("Interractive Map")
	speed = [2,2]
	clock = pygame.time.Clock()
	for i in range(7):
		balls.append(pygame.image.load("ball.jpg"))
	black = 0,0,0
	white = 255,255,255
	print len(balls)
	screen.fill(white)
	for i in range(len(balls)):
		screen.blit(balls[i], balls[i].get_rect())
	pygame.display.flip()
	ballsrect = []
	for i in range(len(balls)):
		ballsrect.append(balls[i].get_rect())
	clock = pygame.time.Clock()
	speeds = []
	for i in range(len(balls)):
		speeds.append( [random.random()*2+i, random.random()*2+1 ] )
	print speeds	
	run = True
	
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1 :
					touched = [ b for b in balls if b.get_rect().collidepoint(event.pos)]
					print touched
				if event.button == 1 :
					speed[0] = -speed[0]
				elif event.button == 3 :
					speed[1] = -speed[1]
				elif event.button == 4 :
					speed = [ 2+x for x in speed]
					print speed
				elif event.button == 5 :
					speed = [ max(x-2,1) for x in speed]
					print speed
				else :
					print event
		for i in range(len(ballsrect)):
			ballsrect[i] = ballsrect[i].move(speeds[i])

			if ballsrect[i].left < 0 or ballsrect[i].right > width:
				speeds[i][0] = -speeds[i][0]
			if ballsrect[i].top < 0 or ballsrect[i].bottom > height:
				speeds[i][1] = -speeds[i][1]
		
		screen.fill(white)
		for i in range(len(balls)):
			screen.blit(balls[i], ballsrect[i])
		pygame.display.flip()
		clock.tick(25)


main()
pygame.quit()
sys.exit()
