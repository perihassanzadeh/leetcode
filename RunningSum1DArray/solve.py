class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        returnList=[]
        for item in nums:
            sum+=item
            returnList.append(sum)

        return returnList