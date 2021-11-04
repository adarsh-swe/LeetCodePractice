class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(n, r, u, p):
            if(len(p) == len(n)):
                done = p[:]
                r.append(done)
                return 

            for i in range(len(n)):
                if(u[i]):
                    continue

                u[i] = True 
                p.append(n[i])
                helper(n, r, u, p)
                p.remove(n[i])
                u[i] = False
        
        res = [] 
        if( nums == None or len(nums) == 0):
            return res
    
        used = [False]*len(nums)
        permutation = []
        helper(nums, res, used, permutation)
        return res 
        
        

        
    
            
            