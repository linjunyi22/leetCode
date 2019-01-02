"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""


class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)  # 去重
        lengths = sorted({len(w) for w in words})  # 从小到大排序

        n = len(s)
        dp = [False] * (n + 1)  # 初始化dp
        dp[0] = True
        for i in range(1, n + 1):
            for l in lengths:  # 选择单词依次判断
                if not dp[i] and i - l >= 0:
                    dp[i] = (dp[i - l] and s[i - l: i] in words)
        return dp[-1]

test = Solution().wordBreak('leetcode',["leet", "code"])
print(test)
