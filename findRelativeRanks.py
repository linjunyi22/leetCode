"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
(注：分数越高的选手，排名越靠前。)

示例 1:
输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。

提示:
1.N 是一个正整数并且不会超过 10000。
2.所有运动员的成绩都不相同。
"""


class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        tmp = nums[:]
        nums.sort(reverse = True)
        count = 0
        for i in nums:
            count += 1
            if count == 1:
                tmp[tmp.index(i)] = "Gold Medal"
            elif count == 2:
                tmp[tmp.index(i)] = "Silver Medal"
            elif count == 3:
                tmp[tmp.index(i)] = "Bronze Medal"
            else:
                tmp[tmp.index(i)] = "{}".format(count)
        return tmp

test = Solution().findRelativeRanks([1,2,3,4,5])
print(test)
