"""
724. 寻找数组的中心索引
Given an array of integers nums, write a method that returns the "pivot" index of this array.
We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

示例 1:
输入: 
nums = [1, 7, 3, 6, 5, 6]
输出: 3

解释: 
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。

示例 2:
输入: 
nums = [1, 2, 3]
输出: -1

解释: 
数组中不存在满足此条件的中心索引。

说明:
1.nums 的长度范围为 [0, 10000]。
2.任何一个 nums[i] 将会是一个范围在 [-1000, 1000]的整数。

"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:  # 数组长度少于3，不符题目要求，直接返回-1，
            return -1
        if sum(nums[1:]) == 0: # 有可能在 1 ~ len(nums) 这个区间的和为零，直接返回首元素下标。
            return 0

        # 取中间索引左右的和，依次遍历，左加右减，筛选出符合要求的下标或返回-1
        l_sum = nums[0]
        r_sum = sum(nums[2:])
        for i in range(1,len(nums) - 1):
            if l_sum == r_sum:
                return i
            else:
                l_sum += nums[i]
                r_sum -= nums[i+1]

        if sum(nums[0:len(nums) - 1]) == 0: # 有可能在 0 ~ len(nums) -1 这个区间的和为零，直接返回末元素下标。
            return len(nums) - 1
        return -1

test = Solution().pivotIndex([-1,-1,1,1,-1,0])
print(test)
