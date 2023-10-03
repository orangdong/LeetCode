class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        output.append([1])
        for i in range(2, numRows + 1):
            pascal = []
            if i > 2:
                prev = output[i - 2]
                pascal.append(1)
                for j in range(1, i -1):
                    if len(prev) < 3:
                        pascal.append(prev[0] + prev[1])
                    else:
                        pascal.append(sum(prev[j-1:j+1]))
                pascal.append(1)
            else:
                pascal.append(1)
                pascal.append(1)
            output.append(pascal)
        return output