
## InteractiveMap
##
## 2015-01-10 ## initial version


import sys, pygame, random

black = 0,0,0
white = 255,255,255
balls = []
ballsrect = []
backgrounds = []

class BackgroundCollection:
	def __init__(self, size):
		self.size = size
		self.backgrounds = []
		self.background = None
	
	def load(self, file):
		img = pygame.image.load(file).convert()
		img = pygame.transform.scale(img, self.size)
		self.backgrounds.append(img)
		
	def load_files(self, files):
		for file in files:
			self.load(file)
		self.select_bg(0)
			
	def select_bg(self, id):
		id = min(id, len(self.backgrounds)-1)
		id = max(0,id)
		self.background = self.backgrounds[id]
	def blit(self, screen):
		screen.blit(self.background, [0,0])

class PlayerCollection:
	def __init__(self):
		self.players = []
		self.players_rect = []
		self.group_mode = False
		self.collision = -1
		
	def load(self, file):
		img = pygame.image.load(file).convert()
		self.players.append(img)
		self.players_rect.append(img.get_rect())
	
	def load_files(self, files):
		for file in files:
			self.load(file)
			
	def move(self, id, to):
		self.players_rect[id].x = to[0] - self.players_rect[id].width/2
		self.players_rect[id].y = to[1] - self.players_rect[id].height/2

	def collide(self, pos):
		self.collision = -1
		if self.group_mode:
			r = range(1)
		else:
			r = range(1,len(self.players_rect))
		print r
		for p in r :
			if self.players_rect[p].collidepoint(pos) :
				self.collision = p
				exit
		return (self.collision >= 0)
	
	def blit(self, screen):
		if self.group_mode:
			screen.blit(self.players[0], self.players_rect[0])
		else:
			for i in range(1,len(self.players)):
				screen.blit(self.players[i], self.players_rect[i])

def load_balls():
	balls.append(pygame.image.load('ball1.gif'))
	balls.append(pygame.image.load('ball2.gif'))
	balls.append(pygame.image.load('ball3.gif'))
	balls.append(pygame.image.load('ball4.gif'))
	for i in range(len(balls)):
		ballsrect.append(balls[i].get_rect())

def refresh_display_old(screen, background):
	screen.fill(white)
	screen.blit(background, [0,0])
	for i in range(len(balls)):
		screen.blit(balls[i], ballsrect[i])
	pygame.display.flip()

def refresh_display(screen, objects):
	screen.fill(white)
	for o in objects:
		o.blit(screen)
	pygame.display.flip()


def main():
	pygame.init()
	dinfo = pygame.display.Info()
	size = width, height = dinfo.current_w-50, dinfo.current_h -50
	screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
	pygame.display.set_caption("Interractive Map")

	bg = BackgroundCollection(size)
	bg.load_files(['background0.jpg', 'background1.jpg'])
	load_balls()
	players = PlayerCollection()
	players.load_files(['ball.jpg', 'ball1.gif', 'ball2.gif', 'ball3.gif', 'ball4.gif'])
	#refresh_display(screen, bg.background) #backgrounds[curr_background])
	refresh_display(screen, [bg, players]) #backgrounds[curr_background])
	clock = pygame.time.Clock()

	run = True
	moving = False
	to_move = 0
	
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1 :
				    if players.collide(event.pos):
						print "collision", players.collision
						moving = True
						to_move = players.collision
#					if moving :
#						print "moving"
#					else :
#						to_move = -1
#						for b in range(len(ballsrect)) :
#							if ballsrect[b].collidepoint(event.pos) :
#								to_move = b
#								exit
#						moving = (to_move >= 0)
			if event.type == pygame.MOUSEBUTTONUP :
				if event.button == 1 :
					moving = False
			if event.type == pygame.MOUSEMOTION and moving :
				#ballsrect[to_move].x = event.pos[0] - ballsrect[to_move].width/2
				#ballsrect[to_move].y = event.pos[1] - ballsrect[to_move].height/2
				players.move(to_move, event.pos)
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_ESCAPE:
					run = False
				if event.key == pygame.K_g:
					players.group_mode = not players.group_mode
				if event.key == pygame.K_1:
					curr_background = 0
					bg.select_bg(0)
				if event.key == pygame.K_2:
					curr_background = min(1,len(backgrounds)-1)
					bg.select_bg(1)
				if event.key == pygame.K_3:
					curr_background = min(2,len(backgrounds)-1)
					bg.select_bg(2)
		
		#refresh_display(screen, bg.background) #backgrounds[curr_background])
		refresh_display(screen, [bg, players]) #backgrounds[curr_background])
		clock.tick(25)

if __name__ == '__main__':
	main()
	pygame.quit()
	sys.exit()
