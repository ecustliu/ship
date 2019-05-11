import sys
import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
import pygame
from pygame.sprite import Group
from alien import Alien
def run_game():
	pygame.init()
	ai_seetings = Settings()
	screen = pygame.display.set_mode(
		(ai_seetings.screen_width,ai_seetings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	ship = Ship(ai_seetings,screen)
	bullets = Group()
	aliens = Group()

	#创建外星人群
	gf.create_fleet(ai_seetings,screen,aliens)

	# alien = Alien(ai_seetings,screen)
	while True:
		gf.check_events(ai_seetings,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_bullets(bullets)
		#每次循环时都重绘屏幕
		gf.update_screen(ai_seetings,screen,ship,aliens,bullets)

run_game()  