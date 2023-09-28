class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        def sortEl(n):
            return n == val
        nums.sort(key=sortEl)
        j =  0
        for i in range(len(nums)):
            if(nums[i] != val):
                j+=1
            
        return j