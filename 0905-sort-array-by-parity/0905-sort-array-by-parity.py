class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        
        for x in range(len(nums)):
            if(nums[x] % 2 == 0):
                even.append(nums[x])
            else:
                odd.append(nums[x])
        even.extend(odd)
        return even