class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binToDec(s):
            i = 0
            total = 0
            for j in range(len(s) - 1, -1, -1):
                pows = 0
                if s[j] == "1":
                    pows = 2**i
                i+=1
                total += pows
            return total
        
        def decToBin(i, result):
            if(i <= 0):
                return result[::-1] if result != "" else "0"
            
            strs = result + str(i%2)
            return decToBin(i//2, strs)
            
        sums = binToDec(a) + binToDec(b)
        return decToBin(sums, '') 