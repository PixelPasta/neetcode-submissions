class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = 1
        for l in range(1, len(nums)):
            if nums[l] == nums[l-1]:
                continue
            nums[r] = nums[l]
            r+=1
        return r
