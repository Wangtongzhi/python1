import pygame
from plant_sprites import *

class PlantGame(object):
    """飞机大战主游戏"""
    def __init__(self):
        print("游戏初始化")
        #创建游戏窗口
        self.screen=pygame.display.set_mode(SCREEN_RECT.size)
        #创建游戏时钟
        self.clock=pygame.time.Clock()
        # 调用私有方法，创建精灵和精灵组
        self.__create_sprites()
        # 设置定时器事件 创建敌人 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌人精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵和精灵组
        self.hero=Hero()
        self.hero_group=pygame.sprite.Group(self.hero)
    def start_game(self):
        print("开始游戏")
        while True:
        # 1设置刷新频率
            self.clock.tick(FRAME_PER_SC)
        # 2事件监听
            self.__event_handlef()
        # 3碰撞检测
            self.__check_collide()
        # 4更新绘制精灵组
            self.__upde_sprites()
        # 5更新显示
            pygame.display.update()
    def __event_handlef(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlantGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌人来")
                # 创建敌人精灵
                enemy = Enemy()
                #  将精灵添加到精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed=2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0
    def __check_collide(self):
        pygame.sprite.groupcollide(self.enemy_group, self.hero.bullets, True, True, collided=None)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True, collided=None)
        if len(enemies) > 0:
            self.hero.kill()
            PlantGame.__game_over()
    def __upde_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()
if __name__=='__main__':
    game = PlantGame()
    game.start_game()
    