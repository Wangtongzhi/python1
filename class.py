class HouseItem():
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s] 占地 &.2f 平米" % (self.name, self.area)


class House():
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list=[]
    def __str__(self):
        return ("户型%s\n总面积%.2f剩余面积为%.2f\n家具为%s"
            % (self.house_type, self.area, self.free_area, self.item_list))
    def add_item(self, item):
        if item.area > self.free_area:
            print("太大了，%s添加进不去" %item.name)
            return
        self.item_list.append(item.name)
        self.free_area -= item.area

bed = HouseItem("席梦思", 5)
chest = HouseItem("如家", 200)
table = HouseItem("桌子", 10)
my_home = House("三室一厅", 100)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
