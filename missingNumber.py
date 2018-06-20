"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

示例 1:
输入: [3,0,1]
输出: 2

示例 2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8

"""


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums:
        	return 0
        nums.sort()
        for i in range(len(nums)-1):
        	if nums[i+1] - nums[i] != 1:
        		return nums[i+1] - 1
        return nums[-1] + 1

test = Solution().missingNumber([0,1,2,5,6,4])
print(test)
