# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         orginal_arr = list(nums)
#         sorted_arr = list(nums)
#         sorted_arr.sort()
#         for i in range(len(nums)):
#             if sorted_arr[i] == sorted_arr[i + 1]:
#                 return sorted_arr[i]

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sorted_arr = list(nums)
        sorted_arr.sort()
        left = 0
        right = 1
        while left < len(sorted_arr):
            if sorted_arr[left] == sorted_arr[right]:
                return sorted_arr[left]
            left += 1
            right += 1



        