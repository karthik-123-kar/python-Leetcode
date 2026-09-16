class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_value = max(arr)
        for i in range(len(arr)):
            if arr[i] == max_value:
                return i