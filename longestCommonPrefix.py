"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        min_len_str = min(strs)

        result = ""
        for i in range(len(min_len_str)):
            for j in strs:
                if min_len_str[i] != j[i]:
                    return result
            result += min_len_str[i]
        return result

test = Solution().longestCommonPrefix(["flower","flow","flight"])
print(test)
