"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n):
        self.list = []
        self._gen(0,0,n,"")
        return self.list
    
    def _gen(self,left,right,n,res):
        """
        :type left: int # 代表左括号用了多少个
        :type right: int # 代表右括号用了多少个
        :type n: int # n 对括号
        :type n: list # 结果
        """
        # 采用递归，类似于将括号放到一个小格子里，|(| |)| |(| |)|，就像这样。每种情况都尝试一下，所以时间复杂度是O(2^n)。
        # 在递归过程中判断一下括号是否有用完，及左右括号的大小关系，可以省略掉一些不必要的递归。

        if left == n and right == n: # 左右括号都用完了，就把结果存起来
            self.list.append(res)
            return 
        if left < n: # 左边没用完
            self._gen(left + 1,right,n,res + "(")
        if left > right and right < n: # 右边没用完，而且右边未用完括号数小于左边的，如果不加 left > right的条件，会导致出现 )( 这样的情况，加上后可以保证先放左括号。
            self._gen(left,right + 1,n,res + ")")

if __name__ == '__main__':
    test = Solution().generateParenthesis(5)
    print(test)
