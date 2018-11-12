"""
Given two strings s and t which consist of only lowercase letters.
String t is generated by random shuffling string s and then add one more letter at a random position.
Find the letter that was added in t.

给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母
"""


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l_s = sorted(list(s))
        l_t = sorted(list(t))

        for i in range(len(l_s)):
            if l_s[i] != l_t[i]:
                return l_t[i]
        return l_t[-1]

test = Solution().findTheDifference("aabcd","aabcd")
print(test)
