class Cat():
    def __init__(self,sex,name):
        self.sex = sex
        self.name= name
    def eat(self):
        print("%s猫"%self.sex+"%s吃鱼"%self.name)
    def drink(self):
        print("瞎猫合适")
tom=Cat("GONG","是是是")
# tom.name = "龙龙"
# tom.sex="公"
tom.drink()
tom.eat()