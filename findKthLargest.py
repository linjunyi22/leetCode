"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 先排序，然后切片取反遍历，比较下标值+1是否等于给定值k，符合则返回 value
        nums = sorted(nums)
        for i,v in enumerate(nums[-1:-len(nums)-1:-1]):
        	if i+1 == k:
        		return v


test = Solution().findKthLargest([1,2,3,2,5,2,3],1)
print(test)
