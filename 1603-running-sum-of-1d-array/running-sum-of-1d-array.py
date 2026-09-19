class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            sum = 0
            for j in range(i + 1):
                sum += nums[j]
            result.append(sum)
        return result
    