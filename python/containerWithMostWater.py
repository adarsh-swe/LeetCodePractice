class Solution:
    def maxArea(self, height: List[int]) -> int:
        currMax = 0 
        if (len(height) == 2):
            return min(height[0], height[1])
        
        L=0
        R=len(height)-1
        
        while(L<R):
            currMax = max(currMax,min(height[L],height[R])*(R-L))
            if(height[L] <= height[R]):
                L+=1
            else:
                R-=1
            
        return currMax
        