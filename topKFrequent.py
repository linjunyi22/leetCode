"""
Given a non-empty array of integers, return the k most frequent elements.

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

例如，
给定数组 [1,1,1,2,2,3] , 和 k = 2，返回 [1,2]。

注意：
你可以假设给定的 k 总是合理的，1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        tmp = []
        for j in d:
            tmp.append((j,d[j]))
        tmp = sorted(tmp,key=lambda x:x[1],reverse=True)
        res = [i[0] for i in tmp[:k]]
        return res


if __name__ == '__main__':
    res = Solution().topKFrequent([1,4,3,54,1,5,1,2,3,2,1,3,2,2],2)
    print(res)
