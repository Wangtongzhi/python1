import random
import pygame
# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SC=60
# 创建敌人定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹
HERO_FIRE_EVENT=pygame.USEREVENT +1
class GameSprite(pygame.sprite.Sprite):
# 飞机大战游戏精灵
    def __init__(self, image_name, speed=1):
        # 调用父类方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        # 在屏幕的方向垂直运动
        self.rect.y+=self.speed
class Background(GameSprite):
    # 游戏背景精灵
    def __init__(self, is_alt= False):
        # 1调用父类方法创建精灵
        super().__init__('./images/background.png')
        # 2判断是否是交替图案，如果是需要初始位置
        if is_alt:
            self.rect.y=-self.rect.height
    def update(self):
        #1调用父类的方法实现
        super().update()
        #2判断是否溢出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
class Enemy(GameSprite):
    # 敌人精灵
    def __init__(self):
        # 调用父类方法 创建敌人精灵 指定图片
        super().__init__("./images/enemy1.png")
        # 指定初始速度
        self.speed=random.randint(1,5)
        # 指定随机位置
        self.rect.bottom = 0
        max_x=SCREEN_RECT.width-self.rect.x
        self.rect.x=random.randint(0,max_x)
    def update(self):
        # 调用父类方法 保持垂直飞行
        super().update()
         # 判断是否飞出屏幕 如果是 从精灵组删除敌人
        if self.rect.y >= SCREEN_RECT.height:
            # kill可以将精灵从精灵组组删除，自动销毁
            self.kill()
    def __del__(self):
        # print("销毁了")
        pass
class Hero(GameSprite):
    def __init__(self):
        # 调用父类方法 设置图片和初始位置
        super().__init__("./images/me1.png",0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets=pygame.sprite.Group()
    def update(self):
        self.rect.x += self.speed
        # 控制英雄移动边界
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
    def fire(self):
        for i in(0,1,2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)
class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png",-5)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
    def __del__(self):
        pass



