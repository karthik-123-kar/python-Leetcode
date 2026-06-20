class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums=sorted(nums)
        result = []  
        for _ in range(len(nums)):
            if(nums[_]==target):
                result.append(_)
        return result
        

