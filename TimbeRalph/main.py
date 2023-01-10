import pygame,random

pygame.init()

#Reloj
clock=pygame.time.Clock()

#Pantalla
screen_width=1100
screen_height=700
screen=pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Timperalph")


#Colores
white=(255,255,255)
black=(0,0,0)
png=(38,255,0)

#Coordenadas jugador
ralph1_y=392
ralph2_y=400

ralph_left=330
ralph1_right=630
ralph2_right=592

#Marcador
score=0
def draw_score(surface,text,size,x,y):

	font=pygame.font.SysFont("impact",size)
	text_surface=font.render(text,True,white)
	text_rect=text_surface.get_rect()
	text_rect.midtop=(x,y)
	surface.blit(text_surface,text_rect)

#Fondo
background=pygame.image.load("files/Fondo TimbeRalph.png").convert()
background=pygame.transform.scale(background,(1100,700))

#ramas
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		random_num=random.randrange(0,2)
		if random_num==0:
			self.image=pygame.image.load("files/Enemigo Right.png").convert()
			self.image= pygame.transform.scale(self.image, (160,62))
			self.image.set_colorkey(png)
			self.rect=self.image.get_rect()
			self.rect.x=615
			self.rect.y=40
		elif random_num==1:
			self.image=pygame.image.load("files/Enemigo Left.png").convert()
			self.image= pygame.transform.scale(self.image, (160,62))
			self.image.set_colorkey(png)
			self.rect=self.image.get_rect()
			self.rect.x=296
			self.rect.y=40

	def update(self):
		if self.rect.y>520:
			self.kill()

#Jugador
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image=pygame.image.load("files/ralph left.png").convert()
		self.image= pygame.transform.scale(self.image, (104, 158))
		self.image.set_colorkey(png)
		self.rect=self.image.get_rect()
		self.rect.x=ralph_left
		self.rect.y=ralph2_y-8

	def update(self):
		keystate=pygame.key.get_pressed()
		if keystate[pygame.K_RIGHT]:
			self.rect.x=ralph2_right
			self.image=pygame.image.load("files/ralph right2.png").convert()
			self.image= pygame.transform.scale(self.image, (142, 150))
			self.image.set_colorkey(png)
			self.rect.y=ralph2_y
			self.rect.x=ralph2_right

		if keystate[pygame.K_LEFT]:
			self.rect.x=ralph_left
			self.image=pygame.image.load("files/ralph left2.png").convert()
			self.image= pygame.transform.scale(self.image, (142, 150))
			self.image.set_colorkey(png)
			self.rect.y=ralph2_y

#Lista de sprites
all_sprite_list=pygame.sprite.Group()
ramas_list=pygame.sprite.Group()

#Creamos el objeto ralph con clase player
ralph=Player()
all_sprite_list.add(ralph)

#Creamos enemigo
rama=Enemy()
all_sprite_list.add(rama)
ramas_list.add(rama)

running=True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				pass
			if event.key==pygame.K_RIGHT:
				pass
		if event.type == pygame.KEYUP:

			if event.key==pygame.K_LEFT:
				rama.rect.y+=100
				ralph.image=pygame.image.load("files/ralph left.png").convert()
				ralph.image= pygame.transform.scale(ralph.image, (104, 158))
				ralph.image.set_colorkey(png)
				ralph.rect.y=ralph1_y
				score+=1
				if colision:
					ralph.image=pygame.image.load("files/rip.png").convert()
					ralph.image= pygame.transform.scale(ralph.image, (104, 158))
					ralph.image.set_colorkey(png)
					ralph.rect.y=ralph1_y

			elif event.key==pygame.K_RIGHT:
				rama.rect.y+=100
				ralph.image=pygame.image.load("files/ralph right.png").convert()
				ralph.image= pygame.transform.scale(ralph.image, (104, 158))
				ralph.image.set_colorkey(png)
				ralph.rect.y=ralph1_y
				ralph.rect.x=ralph1_right
				score+=1
				if colision:
					ralph.image=pygame.image.load("files/rip.png").convert()
					ralph.image= pygame.transform.scale(ralph.image, (104, 158))
					ralph.image.set_colorkey(png)
					ralph.rect.y=ralph1_y
					ralph.rect.x=ralph1_right
			
	all_sprite_list.update()

	#Colisiones
	colision = pygame.sprite.spritecollide(ralph,ramas_list, False)

	screen.blit(background,[0,0])

	all_sprite_list.draw(screen)

	#Marcador
	draw_score(screen,str(score),30,793,148)

	pygame.display.flip()
	clock.tick(60)
pygame.quit()