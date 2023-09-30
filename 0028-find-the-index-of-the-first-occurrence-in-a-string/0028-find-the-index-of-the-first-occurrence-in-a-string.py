class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        neeLength = len(needle)
        index = None
        for i in range(len(haystack)):
            if(haystack[i:neeLength + i] == needle):
                index = i
                break;
                
        return index if index != None else -1