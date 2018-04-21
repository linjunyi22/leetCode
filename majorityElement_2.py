"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。 你的算法应该在O(1)空间中以线性时间运行。
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        nums_set = set(nums)
        for i in nums_set: # 线性时间，时间复杂度为 O(n)
            if nums.count(i) > (len(nums)//3):
                result.append(i)
        return result

test = Solution().majorityElement([1,2,3,4,3,3,4,3,6,6,6])
print(test)
