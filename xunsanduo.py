class Gun():
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0
    def add_bullet(self,count):
        self.bullet_count += count
    def shoot(self,shoot_count):
        if self.bullet_count <= 0:
            print("没有子弹了")
            return
        self.bullet_count -= shoot_count
        print("%s射击%d次" %(self.model,self.bullet_count))
class Solider():
    def __init__(self,name):
        self.name = name
        self.gun=None
    def fire(self,a,b):
        if self.gun==None:
            print("%s你的枪呢"%self.name)
            return
        print("%s冲啊"%self.name)
        self.gun.add_bullet(a)
        self.gun.shoot(b)
ak47 = Gun("AK47")
solider = Solider("许三多")
solider.gun = ak47
solider.fire(50, 10)
print(solider.mro)
# print(solider.gun)