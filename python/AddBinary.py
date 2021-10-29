class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s=""
        sum=0
        i = len(a) - 1 
        j = len(b) - 1 
        while(i >=0 or j >=0):
            if(i>=0):
                sum = sum + int(a[i])
            if(j>=0):
                sum = sum + int(b[j])
            s = str(sum % 2 ) + s 
            sum = sum // 2

            i -= 1 
            j -= 1
 
        if(sum != 0):
            s = str(sum) + s 
        return s
        