card_list = []
def show_menu():
    print("*" * 50)
    print("欢迎来到名片管理系统：\n 1新建\n 2显示\n 3查询\n 0退出")
    print("*" * 50)
def new_card():
    print("*" * 50)
    print("新增名片")
    name = input("请输入名字")
    tel = input("请输入电话")
    qq = input("请输入qq")
    email = input("请输入邮箱")
    card_dict = {
        "姓名": name,
        "电话": tel,
        "qq": qq,
        "邮箱": email}
    card_list.append(card_dict)
    print(card_list)
    print("名片添加成功")
def show_all():
    print("*" * 50)
    if len(card_list) == 0:
        print("当前没有任何名片")
        return
    for name in ["姓名", "电话", "qq", "邮箱"]:
        print(name, end="\t\t")
    print("")
    for card_dict in card_list: 
        print(card_dict["姓名"],"\t",card_dict["电话"],"\t",card_dict["qq"],"\t",card_dict["邮箱"])
    print("显示名片成功")
def serch_card():
    serch_name = input("请输入你要查找的人名")
    for card_dict in card_list:
        if card_dict["姓名"] == serch_name:
            print(card_dict["姓名"], "\t", card_dict["电话"], "\t", card_dict["qq"], "\t", card_dict["邮箱"])
            deal_card(card_dict)
            return
        else:
            print("找不到")
def deal_card(find_dict):
    deal = input("执行什么操作呢？1修改2删除3返回上级")
    if deal in ["1", "2", "3"]:
        if deal == "1":
            find_dict["姓名"] = input("姓名")
            find_dict["电话"] = input("电话")
            find_dict["qq"] = input("qq")
            find_dict["邮箱"] = input("邮箱")
            print("修改成功")
        elif deal == "2":
            card_list.remove(find_dict)
            print("删除成功")
        elif deal == "3":
            print("返回上级成功")
        else:
            print("输错了")