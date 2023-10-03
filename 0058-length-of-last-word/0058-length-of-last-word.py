class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        wordFound = False
        for i in range(len(s) -1, -1, -1):
            if(s[i].isalpha()):
                length+=1
                wordFound = True
            else:
                if wordFound:
                    break
        return length