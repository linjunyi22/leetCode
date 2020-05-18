"""
在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）

例子:

输入: N = 1, K = 1
输出: 0

输入: N = 2, K = 1
输出: 0

输入: N = 2, K = 2
输出: 1

输入: N = 4, K = 5
输出: 1

解释:
第一行: 0
第二行: 01
第三行: 0110
第四行: 01101001

注意：
N 的范围 [1, 30].
K 的范围 [1, 2^(N-1)].
"""


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # 字符串左半部分和右半部分对应坐标对应为 1-0 或 0-1
        # 左半部分与 N-1 字符串相同
        # 因此只需求出N-1 的对应部分即可
        if N == 1:
            return 0
        tmp = 2**(N-1) / 2
        if K <= tmp:
            return self.kthGrammar(N-1, K)
        else:
            return 1 - self.kthGrammar(N-1, K - tmp)


if __name__ == "__main__":
    res = Solution().kthGrammar(4, 5)
    print(res)
