"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words. 
You may return the list in any order.

给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
返回所有不常用单词的列表。
您可以按任何顺序返回列表。

示例 1：
输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]

示例 2：
输入：A = "apple apple", B = "banana"
输出：["banana"]
 
提示：
1.0 <= A.length <= 200
2.0 <= B.length <= 200
3.A 和 B 都只包含空格和小写字母。
"""


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A_list = A.split(' ')
        B_list = B.split(' ')
        
        A_list.extend(B_list)
        result = []
        for i in A_list:
        	if A_list.count(i) == 1:
        		result.append(i)
        return result

test = Solution().uncommonFromSentences('this is a apple','this is a banana')
print(test)



