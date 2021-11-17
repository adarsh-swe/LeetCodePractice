class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        dict = {}

        for num in nums: 
            dict[num] = 1


        maxCount = 0
        for num in nums: 
            if (num-1) not in dict:
                currCount = 1
                while((num+1) in dict):
                    currCount += 1 
                    num += 1
                maxCount = max(maxCount,currCount)
        return maxCount