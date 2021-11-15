import math 

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiff = math.inf
        currSum = 0
        prev = []
        
        for i in range(len(nums)):
            if nums[i] in prev:
                continue
            prev.append(nums[i])
            L=i+1
            R=len(nums)-1
            while(L<R):
                threeSum = nums[i] + nums[L] + nums[R]
                if abs(target-threeSum) < minDiff:
                    minDiff = abs(target-threeSum)
                    currSum = threeSum
                if(threeSum <= target):
                    L+=1
                elif(threeSum > target):
                    R-=1
        return currSum