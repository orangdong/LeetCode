class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            
            if w*h > maxArea:
                maxArea = w*h
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
                