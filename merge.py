"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
1.The number of elements initialized in nums1 and nums2 are m and n respectively.
2.You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]

        if len(nums1) > m + n:
            for j in range(len(nums1) - m - n):
                nums1.pop(-j-1)
        nums1.sort()
        print(nums1)

test = Solution().merge([1,2,3,0,0,0,0],3,[2,5,6],3)
print(test)
