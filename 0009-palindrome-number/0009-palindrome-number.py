class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        flag = False
        if num[::-1] == num:
            flag = True
        
        return flag