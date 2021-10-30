class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        """
        BruteForce 
        """
        count = 0 
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if(sum==k):
                    count+=1
        return count


        # left = 0
        # right = 0
        # count = 0 
        # sum = 0

        # while(right < len(nums)):
        #     if sum == k:
        #         count+=1 
        #         sum-=nums[left]
        #         left+=1
        #     elif sum < k:
        #         right +=1 
        #         sum += nums[right]
        #     elif sum > k:
        #         sum-=nums[left]
        #         left+=1

        # return count 