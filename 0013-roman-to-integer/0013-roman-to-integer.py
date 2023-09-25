class Solution:
    def romanToInt(self, s: str) -> int:
        index = []
        rom = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        count = 0
        for i, v in enumerate(s):
            if(i not in index):
                if(i < len(s) - 1):
                    if(v == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X')):
                        count += rom[s[i + 1]] - 1
                        index.append(i)
                        index.append(i + 1)
                    elif(v == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C')):
                        count += rom[s[i + 1]] - 10
                        index.append(i)
                        index.append(i + 1)
                    elif(v == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M')):
                        count += rom[s[i + 1]] - 100
                        index.append(i)
                        index.append(i + 1)
                    else:
                        count += rom[v]
                        index.append(i)
                else:
                    count += rom[v]
                    index.append(i)
        return count