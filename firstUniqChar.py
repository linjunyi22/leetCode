"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 
注意事项：您可以假定该字符串只包含小写字母。
"""


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        tmp = collections.Counter(s)

        for i in range(len(s)):
            if tmp[s[i]] == 1:
                return i
        return -1

test = Solution().firstUniqChar("aadadaad")
print(test)
`