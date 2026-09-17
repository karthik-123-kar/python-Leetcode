class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans ^= num
 
        return ans


# 0 XOR 0 = 0  4 anw 5
# 1 XOR 1 = 0
# 0 XOR 1 = 1
# 1 XOR 0 = 1



# class Solution:
#     def singleNumber(self, nums: List[int]) ->int:
#         n = len(nums)
#         for i in range(n):
#             count = 0
#             for j in range(n):
#                 if nums[i] == nums[j]:
#                     count += 1
#             if count == 1:
#                 return nums[i]