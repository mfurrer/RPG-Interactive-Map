
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
	#for i in range(7):
	#	balls.append(pygame.image.load("ball.jpg"))
	balls.append(pygame.image.load('ball1.gif'))
	balls.append(pygame.image.load('ball2.gif'))
	balls.append(pygame.image.load('ball3.gif'))
	balls.append(pygame.image.load('ball4.gif'))
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

	run = True
	moving = False
	to_move = 0
	
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1 :
					if moving :
						print "moving"
					else :
						to_move = -1
						for b in range(len(ballsrect)) :
							if ballsrect[b].collidepoint(event.pos) :
								to_move = b
								print "moving: ", b
								exit
						moving = (to_move >= 0)
			if event.type == pygame.MOUSEBUTTONUP :
				if event.button == 1 :
					moving = False
			if event.type == pygame.MOUSEMOTION and moving :
				print event.pos, moving, to_move
				ballsrect[to_move].x = event.pos[0] - ballsrect[to_move].width/2
				ballsrect[to_move].y = event.pos[1] - ballsrect[to_move].height/2


		screen.fill(white)
		for i in range(len(balls)):
			screen.blit(balls[i], ballsrect[i])
		pygame.display.flip()
		clock.tick(25)


main()
pygame.quit()
sys.exit()
