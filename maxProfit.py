"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
假设你有一个数组，其中第 i 个元素是一支给定股票第 i 天的价格。
如果您只能完成最多一笔交易（即买入和卖出一股股票），则设计一个算法来找到最大的利润。

示例 1:
输入: [7, 1, 5, 3, 6, 4]
输出: 5
最大利润 = 6-1 = 5（不是 7-1 = 6, 因为卖出价格需要大于买入价格）
 
示例 2:
输入: [7, 6, 4, 3, 1]
输出: 0
在这种情况下, 没有交易完成, 即最大利润为 0。

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
        	return 0

        begin_value = prices[0]
        result = 0
        for p in prices:
            result = max(result, p - begin_value) # 更新后一个值减前一个值
            begin_value = min(begin_value, p)   # 更新最小值
        return result

print(Solution().maxProfit([1,2,3,2,4,1]))
      