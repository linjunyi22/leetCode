"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:
输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if nums == []:
            return []
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i] - 1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i += 1
        res = []
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                res.append(i+1)
        return res

test = Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(test)
