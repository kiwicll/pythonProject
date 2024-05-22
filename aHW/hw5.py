"""

1、定义一个函数，实现在控制台打印n遍唐诗《绝句》，并使用50个星（*）号分隔每一次打印结果，n遍是形参

2、输入要过生日的人的名字，唱生日歌给他听  “祝你生日快乐，祝XXX生日快乐”

3、定义函数：num_max(x, y, z) 返回3个整数的输入最大值

4、定义函数：user_table(name, age, native_place) 函数逻辑是提供3个形参，name、age、native_place，
  native_place籍贯的意思，默认值为汉族，将定义的3个形参以及参数值整合成字典类型，并返回字典结果


5、编写一个函数，判断一个数是否为质数。
"""
# def TangShi(n):
#     a =0
#     while a < (n+1):
#         print("绝句", end="*")
#         a+=n
#     return n
# TangShi(2)

# def BD(name):
#     print(f'祝你生日快乐，祝{name}生日快乐')
# BD(input("请输入名字"))

# def num_max(x, y, z):
#     max_num = x  # 假设x是初始的最大值
#     if y > max_num:  # 如果y比当前的最大值大，则更新最大值
#         max_num = y
#     if z > max_num:  # 如果z比当前的最大值大，则更新最大值
#         max_num = z
#     return max_num  # 返回找到的最大值
#
# print(num_max(1,5,7))

# def user_table(name, age, native_place="汉族"):
#     info={
#         "name":name,
#         "age":age,
#         "native_place":native_place
#     }
#     return info
# print(user_table("chen","19"))


# def print_poem_n_times(n):
#     poem = """
#     两个黄鹂鸣翠柳，
#     一行白鹭上青天。
#     窗含西岭千秋雪，
#     门泊东吴万里船。
#     """
#     separator = "**************************************************"
#
#     for _ in range(n):
#         print(poem)
#         print(separator)
#
#     # 示例使用
# print_poem_n_times(3)

"""
1: 添加键值对
描述：编写一个函数，它接受一个字典和一个键值对(key, value)，将键值对添加到字典中，如果键已存在则更新其值。
"""
def add_or_update_key(dic, key, value):
    # 检查键是否已经在字典中
    if key in dic:
        # 如果键存在，则打印一条消息并更新其值
        print("键 '", key, "' 已存在于字典中，正在更新其值...")
        dic[key] = value
    else:
        # 如果键不存在，则打印一条消息并添加新的键值对
        print("键 '", key, "' 不存在于字典中，正在添加新的键值对...")
        dic[key] = value

        # 打印更新后的字典内容
    print("更新后的字典内容:")
    for k, v in dic.items():
        print("键: ", k, " 值: ", v)

    # 示例使用
my_dict = {'a': 1, 'b': 2}
print("原始字典内容:")
for k, v in my_dict.items():
    print("键: ", k, " 值: ", v)

# 添加新键值对
add_or_update_key(my_dict, 'c', 3)
# 更新已存在的键值对
add_or_update_key(my_dict, 'a', 5)

