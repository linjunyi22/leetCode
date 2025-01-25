package main

import "fmt"

/*
题目：合并两个有序数组
算法思路：
1. 使用双指针法从后向前遍历两个数组
2. 设置三个指针：
   - i: 指向 nums1 有效元素的末尾
   - j: 指向 nums2 的末尾
   - k: 指向 nums1 数组的末尾位置
3. 比较两个指针指向的元素大小：
   - 如果 nums1[i] >= nums2[j]，则将 nums1[i] 放入 k 位置
   - 否则将 nums2[j] 放入 k 位置
4. 移动对应指针，继续比较直到 j < 0

图解过程：
初始状态：
nums1 = [1, 2, 3, 0, 0, 0]  m = 3
nums2 = [2, 5, 6]           n = 3
指针位置：i = 2, j = 2, k = 5

步骤1: 比较 nums1[i]=3 和 nums2[j]=6
nums1[i]=3 < nums2[j]=6，取nums2[j]放入k位置
[1, 2, 3, 0, 0, 6]  ←放入6
                 ↑
                 k
i=2, j=1, k=4

步骤2: 比较 nums1[i]=3 和 nums2[j]=5
nums1[i]=3 < nums2[j]=5，取nums2[j]放入k位置
[1, 2, 3, 0, 5, 6]  ←放入5
              ↑
              k
i=2, j=0, k=3

步骤3: 比较 nums1[i]=3 和 nums2[j]=2
nums1[i]=3 > nums2[j]=2，取nums1[i]放入k位置
[1, 2, 3, 3, 5, 6]  ←放入3
           ↑
           k
i=1, j=0, k=2

步骤4: 比较 nums1[i]=2 和 nums2[j]=2
nums1[i]=2 >= nums2[j]=2，取nums1[i]放入k位置
[1, 2, 2, 3, 5, 6]  ←放入2
        ↑
        k
i=0, j=0, k=1

步骤5: 比较 nums1[i]=1 和 nums2[j]=2
nums1[i]=1 < nums2[j]=2，取nums2[j]放入k位置
[1, 1, 2, 3, 5, 6]  ←放入2
     ↑
     k
i=-1, j=-1, k=0

最终结果：[1, 2, 2, 3, 5, 6]

算法特点：
1. 从后向前比较和填充，避免了额外的空间使用
2. 通过比较两个数组的元素，每次选择较大的放在末尾
3. 当j<0时结束，说明nums2的所有元素都已放入nums1
4. 如果nums2还有剩余元素，会自动被放入nums1的前面
*/

func merge(nums1 []int, m int, nums2 []int, n int) {
	i, j := m-1, n-1
	k := len(nums1) - 1

	for j >= 0 {
		if i >= 0 && nums1[i] >= nums2[j] {
			nums1[k] = nums1[i]
			i--
		} else {
			nums1[k] = nums2[j]
			j--
		}
		k--
	}
	return
}

func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	nums2 := []int{2, 5, 6}
	merge(nums1, 3, nums2, 3)
	fmt.Println(nums1)
}
