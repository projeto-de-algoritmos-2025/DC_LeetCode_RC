from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        target_index = k - 1
        
        while left <= right:
            pivot = self.median_of_medians(nums, left, right)
            lt_end, gt_start = self.partition_3_way(nums, left, right, pivot)
            
            if target_index >= lt_end and target_index <= gt_start:
                return nums[target_index]
            elif target_index < lt_end:
                right = lt_end - 1
            else:
                left = gt_start + 1
        
        return -1

    def median_of_medians(self, nums: List[int], left: int, right: int) -> int:
        n = right - left + 1
        if n <= 5:
            sub_array = sorted(nums[left:right+1])
            return sub_array[len(sub_array) // 2]

        medians = []
        for i in range(left, right + 1, 5):
            chunk_end = min(i + 4, right)
            sub_chunk = sorted(nums[i:chunk_end+1])
            medians.append(sub_chunk[len(sub_chunk) // 2])

        return self.median_of_medians(medians, 0, len(medians) - 1)

    def partition_3_way(self, nums: List[int], left: int, right: int, pivot: int) -> tuple[int, int]:
        i, j, n = left, left, right
        
        while j <= n:
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] < pivot:
                nums[j], nums[n] = nums[n], nums[j]
                n -= 1
            else:
                j += 1
        
        return i, n

# Exemplo de uso:
solver = Solution()
nums_tle = [1,2,3,4,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
k_tle = 2
print(f"O {k_tle}º maior elemento é: {solver.findKthLargest(nums_tle, k_tle)}")