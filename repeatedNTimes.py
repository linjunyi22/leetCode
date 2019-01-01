"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
返回重复了 N 次的那个元素。

示例 1：
输入：[1,2,3,3]
输出：3

示例 2：
输入：[2,1,2,5,3,2]
输出：2

示例 3：
输入：[5,1,5,2,5,3,5,4]
输出：5

提示：
1.4 <= A.length <= 10000
2.0 <= A[i] < 10000
3.A.length 为偶数
"""


class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #有一个数重复了N遍，总数为2N，因此未重复的数有N个，而不同的元素总共才 N+1 个，所有其他数字都只有一个，因此有重复的就是那个重复了N遍的数字。
        set_ = set()
        for i in A:
            if i not in set_:
                set_.add(i)
            else:
                return i

test = Solution().repeatedNTimes([1,2,3,3])
print(test)
