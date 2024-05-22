res = {
"responseTime":36,
"noteBodies":[
        {
            "summary":"K+7KGjCoDl3fIwnxXfQPIQ==",
            "noteId":"458114392903b8e164f1d583fb63b949",
            "infoNoteId":"458114392903b8e164f1d583fb63b949",
            "bodyType":0,
            "body":"Arrvft6YZvdqji9HTZ0TLgpzU2a4zB/Nz+qJR0NWdIM=",
            "contentVersion":1,
            "contentUpdateTime":1686818813993,
            "valid":0
        },
        {
            "summary":"K+7KGjCoDl3fIwnxXfQPIQ==",
            "noteId":"458114392903b8e164f1d583fb6b9123",
            "infoNoteId":"458114392903b8e164f1d583fb63b949",
            "bodyType":0,
            "body":"Arrvft6YZvdqji9HTZ0TLgpzU2a4zB/Nz+qJR0NWdIM=",
            "contentVersion":1,
            "contentUpdateTime":2686818813993,
            "valid":0
        },
        {
            "summary":"K+7KGjCoDl3fIwnxXfQPIQ==",
            "noteId":"658114392903b52844f1d583fb63b949",
            "infoNoteId":"458114392903b8e164f1d583fb63b949",
            "bodyType":0,
            "body":"Arrvft6YZvdqji9HTZ0TLgpzU2a4zB/Nz+qJR0NWdIM=",
            "contentVersion":1,
            "contentUpdateTime":3686818813993,
            "valid":1
        },
        {
            "summary": "K+7KGjCoDl3fIwnxXfQPIQ==",
            "noteId": "6458114392903b8e1641123fb63b949",
            "infoNoteId": "458114392903b8e164f1d583fb63b949",
            "bodyType": 0,
            "body": "Arrvft6YZvdqji9HTZ0TLgpzU2a4zB/Nz+qJR0NWdIM=",
            "contentVersion": 1,
            "contentUpdateTime": 4686818813993,
            "valid": 0
        }
    ]
}
# lst = res["noteBodies"]
# b=[]
# for i in lst:
#     if i.get("contentUpdateTime") is not None:
#         c=i["contentUpdateTime"]
#         b.append(c)
# b.sort()
# print(b)

lst = res["noteBodies"]
b=[]
for i in lst:
    if i.get("valid") !=0:
        c=i["noteId"]
        b.append(c)
print(b)

# 获取"noteBodies"列表
lst = res["noteBodies"]

# 创建一个空列表，用于存储满足条件的noteId
b = []
# 遍历"noteBodies"列表中的每一个元素
for i in lst:
    # 检查当前元素的"valid"字段是否不等于0
    if i.get("valid") != 0:
        # 如果不等于0，则获取该元素的"noteId"字段
        c = i["noteId"]
        # 将noteId添加到结果列表b中
        b.append(c)
    # 打印结果列表
print(b)

# valid_note_ids = res["noteId"]
# for note in res["noteBodies"]
#     if note["valid"] != 0
# print(valid_note_ids)