# 647. 回文子串
"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

提示：

输入的字符串长度不会超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 暴力法，直接计算每个子串是否是回文串，时间复杂度为 O(n^2)
class Solution:
    def isPalindrome(self, s):
        if s == "" or len(s) == 1:
            return True

        length = len(s)
        for i in range(0, length // 2):
            if s[i] != s[length - i - 1]:
                return False
        return True

    def countSubstrings(self, s: str) -> int:
        if len(set(s)) == 1:
            return sum(range(1, len(s) + 1))

        res = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                res += 1
                break
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    res += 1
        return res
