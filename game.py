#подключение модулей, переменные (Делает Чекерес Владислав)
from random import randint
from pygame import*
font.init()

font = font.Font(None, 72)
win_width = 800
win_height = 600
left_bound = win_width / 40
right_bound = win_width - 8 * left_bound
shift = 0

x_start = 20
y_start = 10

img_file_back = 'bg.jpg'
img_file_hero = 'player.png'
img_file_enemy = 'sprite.png' 
img_file_bomb = 'bomb.png'
img_file_door = 'door.png'
img_wall = 'wall.png'

FPS = 60

C_WHITE = (255, 255, 255)
C_DARK = (48, 48, 0)
C_YELLOW = (255, 255, 87)
C_GREEN = (32, 128, 32)
C_RED = (255, 0, 0)
C_BLACK = (0, 0, 0)

#финальный спрайт (Делает Ширяев Андрей)
class FinalSprite(sprite.Sprite):
    def _init_(self, player_image, player_x, player_y, player_speed):
        sprite.Sprite._init_ (self)
        self.image = transform.scale(image.load(player_image), (100, 100)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y
#главный герой свойтва (Делает Кривша Анатолий)

















#главный герой методы (Делает Кривша Анатолий)






































#класс стен (Делает Сьомкин Владислав)










#Класс врагов
class Enemy(sprite.Sprite): # - враг
    def __init__(self, x=20, y=0, filename=img_file_enemy, width=60, height=60):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(filename), (width, height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        '''перемещает персонажа, применяя текущюу горизонтаьную и вертикальную скорость'''
    def update(self):
        if self.rect.x <= 300:
            self.side = 'right'
        if self.rect.x >= 600:
            self.side = 'left'
        if self.side == "left":
            self.rect.x -= 5
        else:
            self.rect.x += 5

#запуск игры (Делает Лущик Артем)
display.set_caption("ARCADA")
window = display.set_mode([win_width, win_height])
back = transform.scale(image.load(img_file_back).convert(), (win_width, win_height))
all_sprites = sprite.Group()
barriers = sprite.Group()
enemies = sprite.Group()
bombs = sprite.Group()
robin = Hero(img_file_hero)
all_sprites.add(robin)

#создание стен









#создаем врагов, добавлям их:
en = Enemy(300, 330)
all_sprites.add(en)
enemies.add(en)


#создаем мины, добавляем их:
bomb = Enemy(250, 200, 'bomb23.png', 60, 60)
bombs.add(bomb) #в список всех спрайтов бомбы не добавляем, будем рисовать их отдельной командой
                #так легко сможем подрывать бомбы, а также делаем их неподвижными, update() не вызывается

#создаем финальный спрайт, добавляем его:
door = FinalSprite('door.png', win_width + 500, win_height - 150, 0)
all_sprites.add(door)

#основной цикл игры, управление (Делает --)






















#В цикле пока не финиш (Делает --)



























#Конец игры (Делает ---)
