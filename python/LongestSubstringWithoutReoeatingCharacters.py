class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        currMAX = 0 
        
        if len(s) == 0:
            return 0
        
        for i in range(len(s)):
            currString = []
            next = i+1 
            foundRepeat = False

            while( not foundRepeat and next < len(s)):
                if(s[i] == s[next]):
                    foundRepeat = True
                else:
                    currString.append(s[i])
                
            if(len(currString) > currMax):
                currMax = len(currString)

        return currMax