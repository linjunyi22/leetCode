"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词

"""


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # 生成每一行序列
        line0 = list('qwertyuiop')
        line1 = list('asdfghjkl')
        line2 = list('zxcvbnm')
        result = []

        # 如果单词中的字母不在同一行，那么会出现x+y+z 大于1的情况。
        for word in words:
            x,y,z = 0,0,0
            for i in word:
                if i.lower() in line0:
                    x = 1
                if i.lower() in line1:
                    y = 1
                if i.lower() in line2:
                    z = 1

            if x+y+z == 1:
                result.append(word)
        return result

test = Solution().findWords(['qwer','asdfghjkl','yhnuifds','asdfahkg'])
print(test)
