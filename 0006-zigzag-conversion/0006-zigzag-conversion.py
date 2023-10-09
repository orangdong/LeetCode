class Solution:
    def convert(self, s: str, numRows: int) -> str:
        string =''
        
        if numRows > 1:
            for i in range(numRows):
                space = (numRows - 1) * 2
                for j in range(i, len(s), space):
                    char_space = space - (2 * i)
                    string += s[j]
                    if i > 0 and i < numRows - 1 and j + char_space < len(s):
                        string += s[char_space + j]
        else:
            string = s
                
        return string               