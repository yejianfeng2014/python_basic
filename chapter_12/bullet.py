import  pygame
from  pygame.sprite import  Sprite

class Bullet(Sprite):

    '''一个对飞行的子弹管理的类'''

    def __init__(self,ai_settings,screen ,ship):
        '''在飞船的所处的位置创建一个子弹对象'''
        super(Bullet,self,).__init__()

        self.screen = screen

        # 在0，0 出绘制一个子弹的矩形，在设置正确的位置

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed_factor


    def update(self):
        '''向上移动子弹'''

        self.y -= self.speed_factor
        #更新表示子弹的rect 的位置

        self.rect.y = self.y

    def draw_bullet(self):

        '''在屏幕上绘制子弹'''

        pygame.draw.rect(self.screen,self.color,self.rect)




