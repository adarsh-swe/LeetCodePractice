class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1: 
            return s 
        x = [[] for i in range(numRows)]
        counter = 0
        inc = 1 
        res = "" 
        
        for i in range(len(s)):
            x[counter].append(s[i])
            
            if counter == numRows-1:
                inc = -1 
            if counter == 0:
                inc = 1
            counter+=inc
            
        for i in range(len(x)):
            for j in range (len(x[i])):
                res += x[i][j]
            
        return res 