'''
// 股票价格是随时间波动的，现在有一个股票价格的时问序列，要你求出最佳买卖股票的时
间，能获取最多的利润。
// 例如 :Input 股票价格[9,2,5,4,7,4], 最佳买入时间是股票价格为 2
的时候，
// 最佳卖出时间是股票价格为 7 的时候 现在要你写一个雨数，对于传入的股票价
格序列，求出最住买卖时间点和利润
'''
# def max_profit(prices):
#     if not prices:  # 如果价格列表为空，则无法获得利润
#         return 0, None, None
#
#     min_price = prices[0]  # 初始化最低价格为列表的第一个元素
#     max_profit = 0  # 初始化最大利润为0
#     buy_index = 0  # 初始化买入时间索引为0
#     sell_index = None  # 初始化卖出时间索引为None
#
#     for i, price in enumerate(prices):
#         # 更新最低价格
#         if price < min_price:
#             min_price = price
#             buy_index = i
#             # 计算当前卖出能获得的利润，并更新最大利润和卖出时间
#         profit = price - min_price
#         if profit > max_profit:
#             max_profit = profit
#             sell_index = i
#
#     return max_profit, buy_index, sell_index
#
#
# # 示例使用
# prices = [9, 2, 5, 4, 7, 4]
# profit, buy_time, sell_time = max_profit(prices)
# print(f"最大利润为: {profit}")
# print(f"最佳买入时间是: {buy_time} (对应股票价格: {prices[buy_time]})")
# print(f"最佳卖出时间是: {sell_time} (对应股票价格: {prices[sell_time]})")

#初始化买入卖出及最大利润
buy_time = 0
sell_time = 0
MAX_mn = 0
lst = [10, 9, 5, 4, 20, 0]
#遍历所有可能的买入和卖出时间点组合
for i in range(len(lst)):#买入时间可以是列表的第一个
    for j in range(i + 1, len(lst)):#卖出时间最小是买入后的第一个
        # 计算当前买入和卖出所能获得的利润
        mn = lst[j] - lst[i]
        # 如果当前利润大于已知的最大利润，则更新最大利润以及买入和卖出时间
        if mn > MAX_mn:
            MAX_mn = mn
            buy_time = i
            sell_time = j
print(f'买入时间是{buy_time},买入价格是{lst[buy_time]}')
print(f'卖出时间是{sell_time},卖出价格是{lst[sell_time]}')
print(f'最大利润是{MAX_mn}')
