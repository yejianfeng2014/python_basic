import  sys
import  pygame

def check_event(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:

                #向右移动飞船

                ship.rect.centerx += 1




'''更新屏幕上的图像'''
def update_screen(ai_settings,screen,ship):
    '''每次循环都重新绘图'''

    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #让最近绘制的图像可见

    pygame.display.flip()


