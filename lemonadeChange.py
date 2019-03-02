"""
At a lemonade stand, each lemonade costs $5. 
Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.
Return true if and only if you can provide every customer with correct change.

在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：

输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

示例 2：

输入：[5,5,10]
输出：true

示例 3：

输入：[10,10]
输出：false

示例 4：

输入：[5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。
 
提示：

1.0 <= bills.length <= 10000
2.bills[i] 不是 5 就是 10 或是 20 
"""


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # 记录当前每种面值的剩余数量
        # 一开始做的时候首先就想到了用Map来计数，后来看了其他答案，其实可以直接声明两个变量来计数，这样使用的内存更少一点。
        money_d = {
            "5":0,
            "10":0
        }
        
        for i in bills:
            if i == 5: # 收入5元，无需找零
                money_d['5'] += 1
            elif i == 10: # 收入10元，如果是有5元，找零，否则，无法找零，返回False。
                money_d['10'] += 1
                if not money_d['5']:
                    return False
                else:
                    money_d['5'] -= 1
            else: 
            # 收入20元，如果有10元，找零一张10元和一张5元，
            # 如果没有10元，而5元有3张及以上，找零3张5元。
            # 这里首先应该判断10元的，因为5元能通过组合凑成15。
                if money_d['10'] and money_d['5']:
                    money_d['10'] -= 1
                    money_d['5'] -= 1
                elif money_d['5'] >= 3:
                    money_d['5'] -= 3
                else:
                    return False
        return True

if __name__ == '__main__':
	test = Solution().lemonadeChange([5,5,10,10,20])
	print(test)
