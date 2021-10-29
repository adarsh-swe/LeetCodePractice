class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         MERGE IN PLACE 
#         """
#         if n == 0:
#             return nums1
#         elif m == 0:
#             return nums2
            
#         i=0
#         j=0
        
#         while(i<m):
#             if(j<n and (nums2[j] < nums1[i])):
#                 shift = 1
#                 prevVal = nums1[i]
                
#                 #shifting all by 1 to right side 
#                 while(nums1[i+shift] != 0):
#                     nextVal = nums1[i+shift]
#                     nums1[i+shift] = prevVal
#                     prevVal = nextVal
#                     shift += 1
                    
#                 nums1[i+shift] = prevVal
#                 nums1[i] = nums2[j]
#                 j+=1
#             elif(nums1[i] == 0):
#                 nums1[i] = nums2[j]
#                 i+=1
#                 j+=1
#             else:
#                 i+=1
            
    
        for i in range(n):
            nums1[i+m] = nums2[i]
            
        nums1.sort()