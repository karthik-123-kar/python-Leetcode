class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unq = list(set(nums))
        unq.sort()
        for i in range(len(unq)):
            nums[i] = unq[i]
        return len(unq)