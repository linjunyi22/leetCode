"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1.All letters in this word are capitals, like "USA".
2.All letters in this word are not capitals, like "leetcode".
3.Only the first letter in this word is capital if it has more than one letter, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

1.全部字母都是大写，比如"USA"。
2.单词中所有字母都不是大写，比如"leetcode"。
3.如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:
输入: "USA"
输出: True

示例 2:
输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。

"""

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper() == word:
            return True
        elif word.lower() == word:
            return True
        elif word[0] == word[0].upper() and word[1:].lower() == word[1:]:
            return True
        else:
            return False
        
test0 = Solution().detectCapitalUse('Abc')
test1 = Solution().detectCapitalUse('abc')
test2 = Solution().detectCapitalUse('ABC')
test3 = Solution().detectCapitalUse('aBC')

print(test0, test1, test2 ,test3)
