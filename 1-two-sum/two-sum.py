class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  


        # left=0
        # right=len(nums)-1
        # while left<right:
        #     if nums[left] + nums[right] == target:
        #         return [left,right]
        #     elif nums[left]+nums[right]<target:
        #         left+=1
        #     else:
        #         right-=1
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]