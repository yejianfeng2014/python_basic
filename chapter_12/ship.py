import  pygame

class Ship():
    def __init__(self,screen):
        '''初始化飞船，并且设置其位置'''

        self.screen = screen

        #加载飞船，并且获取其外接矩形

        self.image = pygame.image.load('/img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每一个飞船放入底部


        self.rect.centerx = self.screen_rect.centerx

        self.rect.bottom = self.screen_rect.bottom

        # 是否移动的标志

        self.moving_right = False
        self.moving_left = False
    def update(self):
        '''根据移动标志更新位置'''
        if self.moving_left and self.rect.left >0:
            self.rect.centerx -= 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1


    def blitme(self):
        '''在指定位置绘制飞船'''

        self.screen.built(self.image,self.rect)

