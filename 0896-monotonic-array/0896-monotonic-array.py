class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isDecreasing = False
        isIncreasing = False
        for i in range(1, len(nums)):
            if(nums[i-1] < nums[i]):
                isIncreasing = True
            elif(nums[i-1] > nums[i]):
                isDecreasing = True
        
        return False if isDecreasing and isIncreasing else True