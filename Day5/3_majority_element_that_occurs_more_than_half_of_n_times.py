from typing import List

class Solution:
    def bruteforce_majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for i in range(n):
            
            cnt = 0 
            
            for j in range(n):
                if nums[j] == nums[i]:
                    cnt += 1
            
            if cnt > (n // 2):
                return nums[i]
        
        return -1

    def better_majorityElement(self, nums: List[int]) -> int:        
        n = len(nums)        
        mp = {}
        
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        
        for num, count in mp.items():
            if count > n // 2:
                return num
        
        return -1
    

    def optimal_majorityElement(self, nums: List[int]) -> int:        
        n = len(nums)
        cnt = 0        
        el = 0
        
        for num in nums:
            if cnt == 0:
                cnt = 1
                el = num
            elif el == num:
                cnt += 1
            else:
                cnt -= 1
        
        cnt1 = nums.count(el)
        
        if cnt1 > (n // 2):
            return el
        
        return -1


arr = [2, 2, 1, 1, 1, 2, 2]

sol = Solution()
ans = sol.bruteforce_majorityElement(arr)
print("The majority element is:", ans)

ans = sol.better_majorityElement(arr)
print("The majority element is:", ans)

ans = sol.optimal_majorityElement(arr)
print("The majority element is:", ans)