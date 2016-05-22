from helpers import *

class Game(object):
	def __init__(self, width = 248, height = 441):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.clock = pygame.time.Clock()

	def loadSprites(self):
		self.background = Background()
		self.ground = Ground()
		self.bird = Bird()
		self.backgroundSprites = pygame.sprite.RenderPlain((self.background))
		self.groundSprites = pygame.sprite.RenderPlain((self.ground))
		self.birdSprites = pygame.sprite.RenderPlain((self.bird))

	def draw(self):
		self.backgroundSprites.draw(self.screen)
		self.groundSprites.draw(self.screen)
		self.groundSprites.update()
		self.birdSprites.draw(self.screen)
		self.birdSprites.update()
		pygame.display.flip()

	def getEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					self.bird.jump()

	def mainLoop(self):
		self.loadSprites()
		while 1:
			self.clock.tick(45)
			self.getEvents()
			self.draw()

class Background(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = loadImage('background1.png')

class Ground(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = loadImage('longbg.png')
		self.rect.x = 0
		self.rect.y = 400

	def update(self):
		self.rect.x -= 1
		if self.rect.right <= 248:
			self.reset()

	def reset(self):
		self.rect.left = 0
		
class Bird(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.sprites = ['bird1.png', 'bird2.png', 'bird3.png']
		self.sprite = 0
		self.image, self.rect = loadImage(self.sprites[self.sprite])
		self.rect.centerx = 90
		self.rect.centery = 220
		self.jumpSpeed = -10
		self.vertSpeed = 0
		self.fallingSpeed = -1
		self.timer = 0

	def update(self): 
		self.animate()
		self.drop()

	def animate(self):
		self.timer += 1

		if self.timer == 8:
			self.image = updateImage(self.sprites[self.sprite])
			self.sprite += 1

			if self.sprite == 3:
				self.sprite = 0

			self.timer = 0

	def drop(self):
		self.rect.centery += self.vertSpeed
		self.vertSpeed -= self.fallingSpeed
			
	def jump(self):
		self.image = updateImage('flap.png')
		self.vertSpeed = self.jumpSpeed

if __name__ == "__main__":
	Game = Game()
	Game.mainLoop()
	
