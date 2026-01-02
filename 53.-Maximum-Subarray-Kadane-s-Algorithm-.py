class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_a=float("-inf")
        # for i in range(len(nums)):
        #     sum_a=0
        #     for j in range(i,len(nums)):
        #         sum_a+=nums[j]
        #         max_a=max(max_a,sum_a)
        #     max_a=max(max_a,sum_a)
        # return max_a 
        max_a=nums[0]
        sum_a=nums[0]
        for i in range(1,len(nums)):
            sum_a=max(nums[i],sum_a+nums[i])
            max_a=max(sum_a,max_a)
        return max_a

        
