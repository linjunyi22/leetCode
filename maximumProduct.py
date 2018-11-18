"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:
输入: [1,2,3]
输出: 6

示例 2:
输入: [1,2,3,4]
输出: 24

注意:
给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
"""


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0] * nums[1] > nums[-2] * nums[-3]:
            return nums[0] * nums[1] * nums[-1]
        return nums[-1] * nums[-2] * nums[-3]

test = Solution().maximumProduct([1,2,3])
print(test)
