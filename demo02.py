# #判断
# # a = 1
# # b = 2
# # if a > b:
# #     print("111")
# # else:
# #     print("222")
# high = {}
# low = {}
# list = ["a", "b", "c", "d", "e", "f", "g"]
# count = 0
# while count < len(list):
#     score = int(input("请输入" + list[count] + "成绩"))
#     if score > 60:
#         high[list[count]]=score
#     else:
#         low[list[count]]=score
#     count = count + 1
# print(high)
# for i in range(1,10):
#     for j in range(1,i + 1):
#         print(i, "X", j, "=", i * j, end="  ")
#     print()
a = 1
while a>0:
    for i in range(1,31):
        print(i)
    for j in range(1,36):
        print(j)
    for k in range(1,4):
        print(k)
