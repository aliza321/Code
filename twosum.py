class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        ans=[]
        for i in range(len(nums)):
            secNum = target-nums[i]
            if(secNum in dic.keys()):
                secIn = nums.index(secNum)
                if(i != secIn):
                    return sorted([i, secIn])
                
            dic.update({nums[i]: i})
        
    