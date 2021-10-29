class Solution:
    def myAtoi(self, s: str) -> int:

        sign = 1
        ans=0
        i = 0

        while i < len(s) and s[i] == " ":
            i+=1
        
        if( i < len(s) and s[i] == "-"):
            sign = -1
            i+=1
        elif(i < len(s) and s[i] == "+"):
            i+=1

        while(i <len(s) and s[i].isnumeric()):
            ans = ans*10 + int(s[i])
            i+=1 

        ans *= sign

        if(ans < -1*pow(2,31)):
            return -1*pow(2,31)
        elif(ans>(pow(2,31)-1)):
            return (pow(2,31)-1)
        else:
            return ans
