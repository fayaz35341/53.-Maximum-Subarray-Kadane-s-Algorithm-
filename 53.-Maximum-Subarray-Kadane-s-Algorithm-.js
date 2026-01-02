/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let max_a=nums[0]
    let sum_a=nums[0]
    for (let i=1; i<nums.length;i++){
        sum_a=Math.max(nums[i],sum_a+nums[i])
        max_a=Math.max(sum_a,max_a)
    }
    return max_a
};
