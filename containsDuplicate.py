"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数应该返回 true。如果每个元素都不相同，则返回 false。

这道题目一开始用的是列表的 count 方法，但提交的时候提示超时了，看了下原来时间复杂度太高了。。。
于是改了个方法，用集合来解决。
"""

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        if len(nums_set) == len(nums):
            return False
        return True
        
        