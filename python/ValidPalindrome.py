class Solution: #THIS IS NOT THE BEST SOLUTION TO THIS QUESTION 
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        end = len(s)-1

        for i in range(len(s)):
            
            if start >= end: 
                return True
            
            while (not s[start].isalnum()) and start < len(s):
                start+=1
                if start >= end: 
                    return True
            while (not s[end].isalnum()) and end >= 0:
                end-=1
                if start >= end: 
                    return True
            if(s[start].lower() == s[end].lower()) and (start < len(s) and end >= 0):
                start+=1
                end -=1 
            else:
                return False
