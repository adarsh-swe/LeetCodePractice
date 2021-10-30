class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        window = ""*len(s)
        if len(t) > len(s):
            return ""
        
        """
        Brute Force Solution 
        """
        
        for i in range(len(s)):
            currWindow = s[i]
            target = t

            if(s[i] not in t):
                continue 

            j = i+1 
            while len(target) > 0 and j < len(s):
                if(s[j] not in target):
                    j+=1
                    currWindow = currWindow + s[j]
                    continue
                
                target = target.replace(s[j], "" , 1)

            if(len(target == 0)):
                if(len(currWindow) < len(window)):
                    window = currWindow
            else:
                return "" 
        return window