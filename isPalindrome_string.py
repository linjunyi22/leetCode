"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: int
        :rtype: bool
        """
        import re

        s = s.lower()
        set_s = set(s)

        if len(s) == 0:
            return True
        elif len(set_s) == 0 and s[0] == ' ':
            return True
        else:
            pattern = re.compile(r'[^a-zA-Z0-9]+') 
            s = re.sub(pattern,'',s) #非数字字母的字符全部换成空字符串
            
            s = list(str(s))
            flag = True # 总对比记录
            for i in range(0,len(s)//2):
                if s[i] == s[len(s)-i-1]:
                    flag_now = True # 每次对比记录
                else:
                    flag_now = False
                flag = flag and flag_now # 上一次记录与当前记录的'与'
            return flag

test = Solution().isPalindrome("race a car")
print(test)
