class Game(object):
    top_score = 0
    @staticmethod
    def show_help():
        print("帮助信息先买枪")
    def __init__(self, player_name):
        self.player_name = player_name
    @classmethod
    def show_top_score(cls):
        print("历史最高击杀%d" %cls.top_score)
    def start_game(self):
        print("%s开始攻击" % self.player_name)
    def kill(self, num):
        if num > Game.top_score:
            Game.top_score=num
        print("%s杀死了%d" %(self.player_name,num))
xiaoming = Game("塞恩")
xiaoli = Game("剑圣")
xiaow = Game("卡特")
xiaoming.kill(50)
xiaoli.kill(20)
xiaow.kill(100)
Game.show_top_score()
      