"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False
        else:
        	x = list(str(x))
        	flag = True # 总对比记录
        	for i in range(0,len(x)//2):
        		if x[i] == x[len(x)-i-1]:
        			flag_now = True # 每次对比记录
        		else:
        			flag_now = False
        		flag = flag and flag_now # 上一次记录与当前记录的'与'
        	return flag

result = Solution().isPalindrome(1223221)
print(result)
