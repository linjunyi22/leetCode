"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return true if and only if the given array A is monotonic.

如果数组是单调递增或单调递减的，那么它是单调的。
如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
当给定的数组 A 是单调数组时返回 true，否则返回 false。

示例 1：

输入：[1,2,2,3]
输出：true

示例 2：

输入：[6,5,4,4]
输出：true

示例 3：

输入：[1,3,2]
输出：false

示例 4：

输入：[1,2,4,5]
输出：true

示例 5：

输入：[1,1,1]
输出：true
 
提示：
1. 1 <= A.length <= 50000
2. -100000 <= A[i] <= 100000
"""


class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        count_p=0
        count_n=0

        for i in range(0,len(A) - 1):
            tmp = A[i+1] - A[i]
            if tmp >= 0:
                count_p += 1
            if tmp <= 0:
                count_n += 1
        if count_p == len(A) - 1 or count_n == len(A) - 1:
            return True
        return False


test = Solution().isMonotonic([1,1,2,1])
print(test)
