"""
1、有变量name=”homin”，使用f-string格式化方式输出文本内容”三好学生：homin，进步之星：homin”

2、有字符串“qweaaa123aaa”，怎么把他倒序输出

3、有字符串“我爱罗，佐助，鸣人”，期望用replace的方法实现”我爱罗X佐助X

4、有字符串“我爱罗，佐助，鸣人”，期望以字符串的形式输出“我爱罗<佐助<鸣人”，用str.split  str.join

5、有字符串“卡卡西，佐助，鸣人”，有用户交互“请输入你最喜欢的火影角色”，如果字符串中未命中返回“你喜欢的角色死了”
"""
name="homin"
a=f'三好学生：{name}，进步之星：{name}'
print(a)

str="qweaaa123aaa"
b=str[::-1]
print(b)

str='我爱罗，佐助，鸣人'
str2=str.replace('，','x')
str3=str2.replace('鸣人','')
print(str3)

# str='我爱罗，佐助，鸣人'
# c=str.split(" ",4)
# print(c)
# d="<".join(c)
# # print(d)

str='卡卡西，佐助，鸣人'
E=input("请输入你最喜欢的火影角色")
if E in str:
    print("输入正确")
else:
    print("你喜欢的角色死了")

# str = "我爱罗，佐助，鸣人"
# names = str.split('，')
# a= '<'.join(names[:])
# b = names[0]+a
# print(b)

s = "我爱罗，佐助，鸣人"
names = s.split('，')
b = '<'.join(names)
print(b)