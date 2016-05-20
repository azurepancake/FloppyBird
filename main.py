from helpers import *

class Game(object):
	def __init__(self, width = 250, height = 441):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))

	def loadSprites(self):
		self.background = Background()
		self.bird = Bird()
		self.backgroundSprites = pygame.sprite.RenderPlain((self.background))
		self.birdSprites = pygame.sprite.RenderPlain((self.bird))

	def mainLoop(self):
		self.loadSprites()
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			self.backgroundSprites.draw(self.screen)
			self.birdSprites.draw(self.screen)
			self.birdSprites.update()
			pygame.display.flip()

class Background(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = loadImage('background1.png')

class Bird(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = loadImage('bird3.png')
		self.rect.centerx = 90
		self.rect.centery = 220
		self.dropRate = 0

	def update(self):
		self.dropRate += 1

		if self.dropRate == 10:
			self.rect.centery += 1
			self.dropRate = 0

	def jump(self):
		self.rect.centery -= 1

if __name__ == "__main__":
	Game = Game()
	Game.mainLoop()
	
