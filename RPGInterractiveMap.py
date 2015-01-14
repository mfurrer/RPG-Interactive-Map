
## InteractiveMap
##
## 2015-01-10 ## initial version


import sys, pygame, random
import os, re

black = 0,0,0
white = 255,255,255

class BackgroundCollection:
	def __init__(self, size):
		self.size = size
		self.backgrounds = []
		self.background = None
		self.background_id = -1
	
	def load(self, file):
		img = pygame.image.load(file).convert()
		#img = pygame.transform.scale(img, self.size)
		self.backgrounds.append(img)
		
	def load_files(self, files):
		for file in files:
			self.load(file)
		self.select_bg(0)
		#self.background_id = 0
			
	def select_bg(self, id):
		id = min(id, len(self.backgrounds)-1)
		id = max(0,id)
		self.background_id = id
		self.background = pygame.transform.smoothscale(self.backgrounds[id], 
														self.size)
		
	def blit(self, screen):
		screen.blit(self.background, [0,0])
	
	def resize(self, size):
		self.size = size
		self.select_bg(self.background_id)

class PlayerCollection:
	def __init__(self, size=(75,75)):
		self.size = size
		self.players = []
		self.players_rect = []
		self.group_mode = False
		self.collision = -1
		
	def load(self, file):
		img = pygame.image.load(file).convert()
		img = pygame.transform.scale(img, self.size)
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

def refresh_display(screen, objects):
	screen.fill(white)
	for o in objects:
		o.blit(screen)
	pygame.display.flip()

def list_img_dir(dir):
	return [os.path.join(dir, file) 
		for file in os.listdir(dir) if re.match('.*\.(gif|jpg|png)', file)]

def main():
	pygame.init()
	dinfo = pygame.display.Info()
	size = width, height = dinfo.current_w-50, dinfo.current_h -50
	screen = pygame.display.set_mode(size, pygame.RESIZABLE)#, pygame.FULLSCREEN)
	pygame.display.set_caption("Interractive Map")

	bg = BackgroundCollection(size)
	bg.load_files(list_img_dir('Backgrounds'))
	#(['background0.jpg', 'background1.jpg'])
	players = PlayerCollection()
	players.group_mode = True
	players.load_files(list_img_dir('Players'))	
	#['ball.jpg', 'ball1.gif', 'ball2.gif', 'ball3.gif', 'ball4.gif'])
	refresh_display(screen, [bg, players])
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
						moving = True
						to_move = players.collision
			if event.type == pygame.MOUSEBUTTONUP :
				if event.button == 1 :
					moving = False
			if event.type == pygame.MOUSEMOTION and moving :
				players.move(to_move, event.pos)
			if event.type == pygame.VIDEORESIZE :
				bg.resize(event.size)
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
					run = False
				if event.key == pygame.K_g:
					players.group_mode = not players.group_mode
				if event.key == pygame.K_1:
					bg.select_bg(0)
				if event.key == pygame.K_2:
					bg.select_bg(1)
				if event.key == pygame.K_3:
					bg.select_bg(2)
		
		refresh_display(screen, [bg, players]) 
		clock.tick(25)

if __name__ == '__main__':
	main()
	pygame.quit()
	sys.exit()
