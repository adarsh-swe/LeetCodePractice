class Solution:
    def addBinary(self, a: str, b: str) -> str:
        longer = a if len(a) >= len(b) else b
        shorter = a if len(a) < len(b) else b
    
        s=""
        sum=0

        LLen = len(longer)
        SLen = len(shorter)

        while(LLen >=0):
            if(SLen >= 0):
                sum = sum + int(longer[LLen]) + int(shorter[SLen])
            else: 
                sum = sum + int(longer[LLen])
            s = str(sum % 2 ) + s 
            sum = sum // 2

            LLen -=1 
            SLen -=1 
 
        if(sum != 0):
            s = str(sum) + s 
        return s
        