"""
Given a non-empty array of integers, return the third maximum number in this array. 
If it does not exist, return the maximum number. 
The time complexity must be in O(n).

示例 1:
输入: [3, 2, 1]
输出: 1
解释: 第三大的数是 1.

示例 2:
输入: [1, 2]
输出: 2
解释: 第三大的数不存在, 所以返回最大的数 2 .

示例 3:
输入: [2, 2, 3, 1]
输出: 1
解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。

"""


class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set_list = list(set(nums))

        if len(nums_set_list) < 3:
        	return max(nums_set_list)

        nums_set_list.sort()
        return nums_set_list[-3]

test = Solution().thirdMax([3,2,1])
print(test)
