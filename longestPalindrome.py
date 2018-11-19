"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:
输入:
"abccccdd"
输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = [(s.count(i),i) for i in set(s)]
        length.sort(reverse=True)

        flag = True
        result = 0

        for one in length:
            if one[0] % 2 == 1 and flag:
                result += one[0]
                flag = False
            elif one[0] % 2 == 0:
                result += one[0]
            else:
                result += one[0] - 1
        return result


test = Solution().longestPalindrome("abcdabcd")
print(test)
