class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s,i,j):
            while (i < j):      
                if(s[i] != s[j]):
                    return False
                i+=1
                j-=1   
            return True 
        
        start = 0 
        end = len(s) - 1
        while (start < end):      
            if(s[start] != s[end]):
                return isPalindrome(s,start+1,end) or isPalindrome(s,start,end-1)

            start+=1
            end-=1
        
        return True