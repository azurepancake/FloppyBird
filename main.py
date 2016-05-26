from helpers import *

class Game(object):
	def __init__(self, width = 248, height = 441):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.clock = pygame.time.Clock()
		self.timer = 0

	def loadSprites(self):
		self.background = Background()
		self.ground = Ground()
		self.bird = Bird()
		self.backgroundSprites = pygame.sprite.RenderPlain((self.background))
		self.groundSprites = pygame.sprite.RenderPlain((self.ground))
		self.birdSprites = pygame.sprite.RenderPlain((self.bird))
		self.pipeSprites = pygame.sprite.RenderPlain()

	def draw(self):
		self.backgroundSprites.draw(self.screen)
		self.pipeSprites.draw(self.screen)
		self.pipeSprites.update()
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

	def time(self):
		self.clock.tick(45)
		self.timer += 1

	def mainLoop(self):
		self.loadSprites()
		while 1:
			self.time()
			self.getEvents()
			self.createPipe()
			self.draw()
			
	def createPipe(self):
		if self.timer >= 100:
			self.length = random.randint(80, 250)
			self.topPipe = Pipes(self.length, "top")
			self.bottomPipe = Pipes((self.length + 120), "bottom")
			self.pipeSprites.add(self.topPipe, self.bottomPipe)
			self.timer = 0

class Background(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = loadImage('background1.png')

class Ground(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = loadImage('ground1.png')
		self.rect.x = 0
		self.rect.y = 400

	def update(self):
		self.scroll()

	def scroll(self):
		self.rect.x -= 1
		if self.rect.right <= 248:
			self.reset()

	def reset(self):
		self.rect.left = 0
		
class Bird(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.flyingSprites = ['bird1.png', 'bird2.png', 'bird3.png']
		self.fallingSprites = ['flap.png', 'bird3.png', 'falling1.png', 'falling2.png', 'falling3.png', 'falling4.png', 'falling5.png']
		self.sprite = 0
		self.image, self.rect = loadImage(self.flyingSprites[self.sprite])
		self.rect.centerx = 90
		self.rect.centery = 220
		self.jumpSpeed = -10
		self.vertSpeed = 0
		self.fallingSpeed = -1
		self.falling = True
		self.timer = 0

	def update(self): 
		self.animate()
		self.fall()

	def animate(self):
		self.timer += 1

		if self.falling == False:

			if self.timer == 8:
				self.image = updateImage(self.flyingSprites[self.sprite])
				self.sprite += 1

				if self.sprite == 3:
					self.sprite = 0

				self.timer = 0

		else:

			if self.timer == 5 and self.sprite < 7:
				self.image = updateImage(self.fallingSprites[self.sprite])
				self.sprite += 1

				self.timer = 0

	def fall(self):
		self.falling = True
		self.rect.centery += self.vertSpeed
		self.vertSpeed -= self.fallingSpeed
			
	def jump(self):
		self.resetAnimation()
		self.falling = False
		self.image = updateImage('flap.png')
		self.vertSpeed = self.jumpSpeed

	def resetAnimation(self):
		self.timer = 0
		self.sprite = 0

class Pipes(pygame.sprite.Sprite):
	def __init__(self, length, pos):
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.length = length

		if self.pos == "top":
			self.image, self.rect = loadImage('topPipe.png')
			self.rect.bottom = self.length
		else:
			self.image, self.rect = loadImage('bottomPipe.png')
			self.rect.top = self.length

		self.rect.left = 250

	def update(self):
		self.rect.x -= 2

	def reset(self):
		self.rect.left = 250

if __name__ == "__main__":
	Game = Game()
	Game.mainLoop()
	
