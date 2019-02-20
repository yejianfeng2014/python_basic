import os
import pygame

import sys

from pygame.locals import *

from  ship import  Ship
from  settings import  Settings

from pygame.sprite import Group

def run_game():
    '''初始化游戏并且创建一个屏幕对象'''

    pygame.init()

    ai_setting = Settings()
    screen = pygame.display.set_mode([ai_setting.screen_width, ai_setting.screen_height])
    pygame.display.set_caption("alien invasion")

    #创建一艘飞船

    ship = Ship(screen)

    # 创建一个存储子弹的编组

     # bullets = Group()


    # 开始游戏的主循环

    while True:

        # screen.fill(ai_setting.bg_color)
        # ship.blitme()

        # 监控鼠标和键盘事件
        for event in pygame.event.get():
            if event.tpye == pygame.QUIT:
                sys.exit()

        # 让最新绘制的屏幕可见
        # pygame.display.flip()


run_game()


class Alien():
    '''表示外星人的类'''

    def __init__(self,ai_settings,screen):

        super(Alien,self).__init__()

        self.screen = screen

        self.ai_settings = ai_settings


