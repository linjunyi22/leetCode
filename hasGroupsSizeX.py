"""
In a deck of cards, each card has an integer written on it.
Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.

给定一副牌，每张牌上都写着一个整数。
此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

1.每组都有 X 张牌。
2.组内所有的牌上都写着相同的整数。
3.仅当你可选的 X >= 2 时返回 true。

示例 1：
输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

示例 2：
输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
"""


class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        import math
        deck_set = set(deck)
        int_count = [deck.count(i) for i in deck_set] #deck 中每个数字出现的次数

        if len(deck) < 2:
            return False
        if len(deck_set) == 1:
            return True

        for i in range(2,int(len(deck)/2) + 1):
        	flag = 0
        	for j in int_count:
        		if j%i != 0:
        			flag = 1
        			break
        	if not flag:
        		return True
       	return False

test = Solution().hasGroupsSizeX([1,1,2,2])
print(test)
