import mingpian_tool
while True:
    mingpian_tool.show_menu()
    action_str = input("请输入你要进行的操作")
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            mingpian_tool.new_card()
        elif action_str == "2":
            mingpian_tool.show_all()
        else:
            mingpian_tool.serch_card()
    elif action_str == "0":
        print("欢迎下次光临")
        break
    else:
        print("输入错误")