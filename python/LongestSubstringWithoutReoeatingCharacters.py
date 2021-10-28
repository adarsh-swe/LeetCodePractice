# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         currMax = 0 
        
#         if len(s) == 0:
#             return 0
        
#         for i in range(len(s)):
#             currString = []
#             next = i
#             foundRepeat = False            
            
#             while((not foundRepeat) and (next < len(s))):
#                 if s[next] in currString: 
#                     foundRepeat = True
#                 else:    
#                     currString.append(s[next])
#                     next+=1
                    
#             if(len(currString) > currMax):
#                 currMax = len(currString)

#         return currMax


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0 
        start = 0
        end = 0
        
        substringWindow = [] 

        while(end < len(s)):
            if(not s[end] in substringWindow):
                substringWindow.append(s[end])
                end+=1
                max_length = max(max_length, len(substringWindow))
            else:
                substringWindow.remove(s[start])
                start +=1
        return max 