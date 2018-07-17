"""
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.
If there aren't two consecutive 1's, return 0.

示例 1：
输入：22
输出：2

解释：
22 的二进制是 0b10110 。
在 22 的二进制表示中，有三个 1，组成两对连续的 1 。
第一对连续的 1 中，两个 1 之间的距离为 2 。
第二对连续的 1 中，两个 1 之间的距离为 1 。
答案取两个距离之中最大的，也就是 2 。
"""


class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        bin_n = bin(N)[2:]
        if bin_n.count('1') == 1:
        	return 0

        tmp = []
        result = []
        for i,v in enumerate(bin_n):
        	if v == '1':
        		tmp.append(i)
        	if len(tmp) == 2:
        		tmp_distance = tmp[1] - tmp[0]
        		tmp.pop(0)
        		result.append(tmp_distance)
        return max(result)

test = Solution().binaryGap(13)
print(test)
