class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lenNums = len(nums)
        enum = list(enumerate(nums))
        pos = None
        
        while lenNums > 1:
            mid = -(lenNums // -2)
            if(enum[mid][1] > target):
                enum = enum[:mid]
                lenNums = len(enum)
            elif(enum[mid][1] == target):
                lenNums = 1
                pos = enum[mid][0]
            elif(enum[mid][1] < target):
                enum = enum[mid:]
                lenNums = len(enum)
        
        if(pos ==None):
            if enum[0][1] > target:
                pos = enum[0][0]
            elif enum[0][1] < target:
                pos = enum[0][0] + 1
            else:
                pos = 0
                
        return pos