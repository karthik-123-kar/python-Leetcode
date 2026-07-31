# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n = len(nums)
#         for i in range(n):
#             count =  0
#             for j in range(n):
#                 if nums[i]==nums[j]:
#                     count += 1
#             if count > n // 2:
#                 return nums[i]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > len(nums) // 2:
                return num
