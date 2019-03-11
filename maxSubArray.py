"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum_ and return its sum_.

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        max_sub_sum = nums[0]
        for num in nums:
            sum_ += num
            if sum_ > max_sub_sum: # 与暂存的最大的数据进行比较
                max_sub_sum = sum_
            if sum_ < 0:
                sum_ = 0
        return max_sub_sum

if __name__ == '__main__':
	test = Solution().maxSubArray([1,2,3,4,5,-1,-2,-3])
	print(test)
