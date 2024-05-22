"""
1.编写函数，统计一个字符串中指定子串出现的次数。
2.编写函数，将一个字符串中的所有单词首字母大写。
3.编写函数，将字符串中的元音字母替换为指定的字符。
4.编写函数，将字符串中的所有空格替换为指定的字符。
5.编写函数，将字符串中的所有数字删除。
6.编写函数，将字符串中的单词进行反转。
7.编写函数，将字符串中的所有大写字母转换为小写字母，将所有小写字母转换为大写字母。
"""


# def StrNum(str1, str):
#     count = 0
#     start_index = 0
#     while True:
#         index = str1.find(str, start_index)
#         if index == -1:
#             break
#         count += 1
#         start_index = index + len(str)
#     return count
#
#
# # 测试函数
# str1 = "llnihao, l2l,l3l,llnihao!"
# str = "ll"
# print(StrNum(str1, str))  # 输出: 3


#Str.title()
# def CountString(str1, str):  # 定义一个函数，接收主串和子串作为参数
#     count = 0  # 初始化计数器为0
#     start_index = 0  # 初始化开始索引为0，表示从主串的开头开始查找
#     while True:  # 开始一个无限循环，直到找到子串或者遍历完整个主串
#         index = str1.find(str, start_index)  # 查找子串在主串中的位置，从start_index开始
#         if index == -1:  # 如果返回-1，表示没有找到子串
#             break  # 跳出循环
#         count += 1  # 找到一个子串，计数器加1
#         start_index = index + len(str)  # 更新开始索引为子串之后的位置
#     return count  # 返回子串在主串中出现的次数
#
# # 测试函数
# str1 = "66679, 67668HHH, 12666, NIHAO!"  # 定义主串
# str = "666"  # 定义子串
# print(CountString(str1, str))  # 调用函数并打印结果，输出应为3


"""编写函数，将一个字符串中的所有单词首字母大写。"""
def Mzm(str):
    str = str.title()
    return str

str = "nihao, 67668HHH, 12666, NIHAO!"
print(Mzm(str))


"""编写函数，将字符串中的所有空格替换为指定的字符"""
def Mzm(str):
    str = str.replace(' ','*')
    return str

str = "nihao 67668HHH 12666   NIH AO!"
print(Mzm(str))




"""5.编写函数，将字符串中的所有数字删除"""
#在Python中，你可以使用正则表达式库re来编写一个函数，删除字符串中的所有数字。下面是一个示例：
import re
def remove_digits(s):
    return re.sub(r'\d', '', s)

# 测试函数
s = "Hello123, World456!"
print(remove_digits(s))  # 输出: Hello, World!

"""在这个函数中，re.sub(r'\d', '', s)使用正则表达式\d来匹配字符串s中的所有数字，并将其替换为空字符串''，
从而删除了所有的数字。\d是一个正则表达式元字符，代表任意一个数字（0-9）。

如果你不想使用正则表达式，你也可以使用字符串的translate()方法和str.maketrans()函数来删除数字："""


def remove_digits(s):
    # 创建一个转换表，将数字映射为空字符
    trans_table = str.maketrans('', '', '0123456789')
    # 使用转换表删除字符串中的数字
    return s.translate(trans_table)


# 测试函数
s = "Hello123, World456!"
print(remove_digits(s))  # 输出: Hello, World!


"""
7.编写函数，将字符串中的所有大写字母转换为小写字母，将所有小写字母转换为大写字母。"""
def Mzm(str):
    str = str.replace(' ','*')
    return str

str = "nihao 67668HHH 12666   NIH AO!"
print(Mzm(str))

