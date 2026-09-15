# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         result = []
#         for i in range(len(nums)): # select one element
#             product = 1
#             for j in range(len(nums)): # check every element
#                 if i != j:             # don't multiply selected element
#                     product = product * nums[j]
#             result.append(product)
#         return result


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        result = [1] * len(nums)

        product = 1

        # left side
        for i in range(len(nums)):
            result[i] = product
            product = product * nums[i]

        # right side
        product = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * product
            product = product * nums[i]

        return result