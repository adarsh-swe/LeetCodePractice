class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) < 3):
            return []

        x = [] 
        nums.sort()

        for i in range(len(nums)):
            target = -1*nums[i]

            j = i + 1 
            d={}
            while(j<len(nums)):
                if((target-nums[j]) in d):
                    newArr = [nums[i], target-nums[j], nums[j]]
                    if not(newArr in x):
                        x.append(newArr)
                else:
                    d[nums[j]] = j    
                j+=1

        return x