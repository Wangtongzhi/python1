class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("蹦跳玩耍")
class TianGou(Dog):
    def game(self):
        print("天上飞起来了啊")
class Person(object):
    def __init__(self,name):
        self.name = name
    def playwithdog(self,dog):
        print("%s和%s一起玩耍" % (self.name, dog.name))
        dog.game()
xiaoming = Person("老王")
dog = TianGou("大黄")
xiaoming.playwithdog(dog)
       
