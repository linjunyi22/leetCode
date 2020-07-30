# 1299. 将每个元素替换为右侧最大元素
"""
给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。
完成所有替换操作后，请你返回这个数组。

示例：

输入：arr = [17,18,5,4,6,1]
输出：[18,6,6,6,1,-1]

提示：

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 暴力解法，效率极低
        res = []
        for i in range(len(arr)):
            if i == len(arr) - 1:
                res.append(-1)
                break
            res.append(max(arr[i+1:]))
        return res


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 从后往前遍历
        # 每次记录当前遍历过的最大的值即可
        res = [-1]*len(arr)
        max_num = -1
        for i in range(len(arr)):
            if i == 0:
                continue
            current_num = arr[-i]
            if current_num > max_num:
                max_num = current_num
            res[-i-1] = max_num
        return res
