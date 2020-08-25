# 338. 比特位计数
"""
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 常规算法
# 计算每个值的二进制然后计数
# 时间复杂度 O(n * k)，k 为每个数统计 1 的个数要进行 k 次操作
# 空间复杂度 O(n)
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = []
        for i in range(0, num + 1):
            ans.append(bin(i).count('1'))
        return ans


# 分奇偶数计算
# 奇数：每个数二进制为 1 的个数比前一个偶数多 1
# 偶数：每个数二进制为 1 的个数与其除以二后的数一致
# 每个数遍历一遍，时间复杂度 O(n)
# 空间复杂度 O(n)
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 1:
                ans[i] = ans[i-1] + 1
            else:
                ans[i] = ans[i//2]
        return ans
