class Person():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return "我叫%s 我有%.2f公斤" %(self.name,self.weight)
    def run(self):
        self.weight-=10
    def eat(self):
        self.weight+=50
xiaoming = Person("小明", 180)
xiaoming.eat()
xiaomei = Person("小美", 80)
xiaomei.run()
print(xiaoming)
print(xiaomei)