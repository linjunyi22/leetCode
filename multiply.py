"""
递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。

示例1:
 输入：A = 1, B = 10
 输出：10

示例2:
 输入：A = 3, B = 4
 输出：12

提示:
保证乘法范围不会溢出

"""


class Solution:
    def helper(self, max_num, min_num):
        if min_num == 1:
            return max_num
        return max_num + self.helper(max_num, min_num - 1)

    def multiply(self, A: int, B: int) -> int:
        if A >= B:
            return self.helper(A, B)
        return self.helper(B, A)


if __name__ == "__main__":
    res = Solution().multiply(1, 10)
    print(res)
