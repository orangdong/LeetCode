class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        j = 0
        new = ''
        for i in word1:
            if(j < len(word2)):
                new += i + word2[j]
            else:
                new += i
            j+=1
        if(len(word2) > j):
            new += word2[j:]
        return new