"""
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.
Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

示例 1：
输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

示例 2：
输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false

示例 3：
输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 
提示：
3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4
"""

class Solution:
    def canThreePartsEqualSum(self, A):
        s=sum(A)
        # 三者相等，那么三者之和能与3 整除
        if s%3!=0:
            return False
        
        target=s//3
        temp=0
        count=0
        # 遍历数组，计算 count = 1 时 part1 的和，count = 2 时 part2 的和。
        # 有 2 部分的和相同且还有元素剩下，那么符合题目要求
        for i,n in enumerate(A):
            temp+=n
            if temp==target:
                count+=1
                if count==2 and i!=len(A)-1:
                    return True
                temp=0
        return False

if __name__ == "__main__":
    l = [1,1,1,1,1]
    result = Solution().canThreePartsEqualSum(l)
    print(result)