# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if(len(nums) < 3):
#             return []

#         x = [] 
#         nums.sort()

#         for i in range(len(nums)):
#             target = -1*nums[i]

#             j = i + 1 
#             d={}
#             while(j<len(nums)):
#                 if((target-nums[j]) in d):
#                     newArr = [nums[i], target-nums[j], nums[j]]
#                     if not(newArr in x):
#                         x.append(newArr)
#                 else:
#                     d[nums[j]] = j    
#                 j+=1

#         return x

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, x in enumerate(nums):
            if(i>0 and x == nums[i-1]):
                continue

            left = i+1
            right = len(nums) -1 

            while(left<right):
                threeSum = x + nums[left] + nums[right]
                if(threeSum > 0):
                    right -=1
                elif(threeSum <0):
                    left +=1 
                else:
                    output.append([x, nums[left], nums[right]])
                    left += 1 
                    while(nums[left-1] == nums[left] and left<right):
                        left+=1
        return output




