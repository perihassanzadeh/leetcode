class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            findd = int(len(nums)/2)
            if target < nums[findd]:
                for x in range(findd+1):
                    if target < nums[x]:
                        return x
            else:
                for x in range(findd, len(nums)):
                    print(x)
                    if target < nums[x]:
                        return x
                    if (target > nums[x]) and (x==len(nums)-1):
                        return x+1