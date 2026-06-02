from typing import List

class Solution:
    def brute_force_maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
        return max_sum

    def better_approach_maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum
    
    def optimal_approach_maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        sum = 0 
        
        for i in range(len(nums)):            
            sum += nums[i]
            if sum > max_sum:
                max_sum = sum 
            
            if sum < 0:
                sum = 0
        return max_sum

    def optimal1_approach_maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        
        sum, start, ansStart, ansEnd = 0, 0, -1, -1
        
        for i in range(len(nums)):
            
            if sum == 0:
                start = i
            
            sum += nums[i] 
            

            if sum > max_sum:
                max_sum = sum
                ansStart = start
                ansEnd = i
            
            if sum < 0:
                sum = 0
                
        return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

sol = Solution()

maxSum = sol.brute_force_maxSubArray(arr)

print("The maximum subarray sum is:", maxSum)


maxSum = sol.better_approach_maxSubArray(arr)

print("The maximum subarray sum is:", maxSum)


maxSum = sol.optimal_approach_maxSubArray(arr)

print("The maximum subarray sum is:", maxSum)


maxSum = sol.optimal1_approach_maxSubArray(arr)

print("The maximum subarray sum is:", maxSum)
