class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = []
        
        for i in nums:
            if i in temp:
                temp.remove(i)
            else:
                temp.append(i)
        return temp[0]