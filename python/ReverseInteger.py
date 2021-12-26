class Solution:
    def reverse(self, x: int) -> int:
        res = "" 
        for i in range(len(str(x))-1,-1,-1):
            if (str(x)[i].isnumeric()):
                res += str(x)[i]
        
        res = int(res)
        if x<0:
            res *= -1
            
        if (res < -1*pow(2,31)) or (res > pow(2,31)-1):
            res = 0
        return res