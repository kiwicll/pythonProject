"""
股票价格是随时间波动的，现在有一个股票价格的时问序列，要你求出最佳买卖股票的时间，能获取最多的利润。
 例如 :Input 股票价格[9,2,5,4,7,4], 最佳买入时间是股票价格为 2的时候，
 最佳卖出时间是股票价格为 7 的时候 现在要你写一个雨数，对于传入的股票价格序列，求出最住买卖时间点和利润
"""
# buy_time = int()
# sell_time = int()
# price = int()
# lst = [9, 2, 5, 4, 7, 4]
# for n in range(len(lst) - 1):
#     for m in range(len(lst) - 1 - n):
#         now_price = lst[n + 1 + m] - lst[n]
#         if price < now_price:
#             price = now_price
#             buy_time = n
#             sell_time = n + 1 + m
# print(buy_time,sell_time,price)

buy_time = 0  # 初始化买入时间为0
sell_time = 0  # 初始化卖出时间为0
max_profit = 0  # 初始化最大利润为0
lst = [9, 2, 5, 4, 7, 4]
# 遍历所有可能的买入和卖出时间点组合
for i in range(len(lst)):#买入时间可以是列表的第一个
    for j in range(i + 1, len(lst)):#卖出时间最小是买入后的第一个，最后的卖出时间是最后一个
        # 计算当前买入和卖出所能获得的利润
        profit = lst[j] - lst[i]
        # 如果当前利润大于已知的最大利润，则更新最大利润以及买入和卖出时间
        if profit > max_profit:
            max_profit = profit
            buy_time = i
            sell_time = j
        # 打印结果
print(f"最佳买入时间: {buy_time}, 最佳卖出时间: {sell_time}, 最大利润: {max_profit}")