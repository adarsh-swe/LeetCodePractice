class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        """
        BruteForce 
        O(n^2)
        """
        """
        count = 0 
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if(sum==k):
                    count+=1
        return count
        """

        """
        Optimized Solution
        O(n)
        """
    
        count = 0 
        sum = 0
        occur = {
            0:1
        }

        for i in range(len(nums)):
            sum += nums[i]
            if (sum-k) in occur:
                count += occur[sum-k]
            if sum in occur: 
                occur[sum] += 1
            else:
                occur[sum] = 1

        
        return count  