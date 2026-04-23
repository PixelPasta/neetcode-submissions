class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                if count > maxCount:
                    maxCount = count
                count = 0
                continue
            elif i == len(nums)-1 and nums[i] == 1:
                count+=1
                if count > maxCount:
                    maxCount = count
                continue
            count+=1
        return maxCount
            
            