"""
1、给1个列表score = [70, 90, 78, 85, 97, 94, 65, 80]  求平均数
答：
2、打印出1到100之间的偶数
答：
3、给一个字符串，去掉所有空格
S = " sfafas asfasf afasf saf asfasf a asf asa"
答：
"""
# score = [70, 90, 78, 85, 97, 94, 65, 80]
# avg=sum(score)/8.0
# print(avg)

# a = 1
# for a in range(0,101):
#     if a%2==0:
#         print(a)

# S = " sfafas asfasf afasf saf asfasf a asf asa"
# str2=S.replace(' ','')
# print(str2)
'''
4、给你一个列表，完成下列题目
已知一个列表：lst = [1, 2, 3 ,4 ,5]

1）求列表的长度
2）判断6是否在表中
3）列表里元素的最大值是多少
4）列表里元素的最小值是多少
5）在列表的末尾新增一个元素20
6）在列表倒数第二的位置新增一个元素18
7）将列表中的值修改成原来2倍
8）移除列表的第二个元素和第四个元素  最终结果[1, 3, 5]
'''
lst = [1, 2, 3 ,4 ,5]
#print(len(lst))
# if 6 in lst:
#     print("在列表中")
# print("不在")
# a=min(lst)
# print(a)
# lst.insert(4,18)
# print(lst)
# for a in lst:
#     b=a*2
#     print(b)
# lst.remove(2)
# lst.pop(2)
# print(lst)
"""
已知一个列表: lst = [13, 15, 15, [275, [276, 279]]]
将列表中的279移除
"""


# def remove_element(lst, element):
#     if isinstance(lst, list):
#         # 遍历列表中的每个元素
#         for i in range(len(lst)):
#             # 如果当前元素是我们要找的元素，则移除它
#             if lst[i] == element:
#                 lst.pop(i)
#                 return True
#                 # 如果当前元素是一个列表，递归地检查它
#             elif isinstance(lst[i], list):
#                 if remove_element(lst[i], element):
#                     return True
#     return False
#
# lst = [13, 15, 15, [275, [276, 279]]]
# if remove_element(lst, 279):
#     print(lst)
# # else:
# #     print("Element not found in the list.")
# # print(lst)


# # #冒泡排序
# def bubble_sort(lst):
#     n = len(lst)
#     for i in range(n):
#         # 添加一个标志位，用于优化，如果在一趟遍历中没有发生交换，说明已经有序，无需继续排序
#         swapped = False
#         for j in range(0, n - i - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#                 swapped = True
#                 # 如果没有交换发生，说明列表已经有序，可以提前结束循环
#         if not swapped:
#             break
#     return lst
#
# lst = [34, 22, 15, 28, 33, 25]
# sorted_lst = bubble_sort(lst)
# print(sorted_lst)

def longest_palindromic_substring(s):
    if not s:
        return ''

    n = len(s)
    # 初始化dp数组
    dp = [[False] * n for _ in range(n)]
    # 初始化最长回文子串的起始位置和长度
    start, max_length = 0, 1

    # 所有单个字符都是回文
    for i in range(n):
        dp[i][i] = True

        # 检查长度为2的子串是否是回文
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

            # 检查长度大于2的子串是否是回文
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length

                    # 返回最长回文子串
    return s[start:start + max_length]
# 示例
s = 'absdhsaidhuuiiuuhasdsa'
print(longest_palindromic_substring(s))