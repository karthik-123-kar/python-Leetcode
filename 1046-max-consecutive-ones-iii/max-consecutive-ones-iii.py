class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        count = 0
        answer = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            answer = max(answer,i - left + 1)
        return answer