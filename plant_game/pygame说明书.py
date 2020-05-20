import pygame
from plant_sprites import*
# 游戏初始化
pygame.init()
# 定义屏幕
screen = pygame.display.set_mode((480, 700))
# 定义背景
bg = pygame.image.load("./images/background.png")
# 定义飞机
hero=pygame.image.load("./images/me1.png")
screen.blit(bg, (0, 0))
screen.blit(hero,(150,500))
pygame.display.update()
clock = pygame.time.Clock()
# 定义rect记录飞机初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)
# 创建敌人精灵
enemy=GameSprite("./images/enemy1.png")
# 创建敌人精灵组
enemy_group = pygame.sprite.Group(enemy)

# 游戏循环开始
while True:
    # 控制游戏循环内部代码执行频率
    clock.tick(60)
    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list)>0:
        print(event_list)
    # 修改飞机位置
    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y=700
    #调用bilt方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero, hero_rect)
    # 让精灵组调用两个方法 update draw
    # 让组中所有精灵更新位置
    enemy_group.update()
    # 在screen上绘制所有的精灵
    enemy_group.draw(screen)
    #调用update方法更新显示
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()