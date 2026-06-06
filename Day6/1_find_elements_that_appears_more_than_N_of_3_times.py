from typing import List
from collections import defaultdict

class Solution:
    def bruteforce_majorityElementTwo(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        result = []
        
        for i in range(n):
            if len(result) == 0 or result[0] != nums[i]:
                
                cnt = 0
                
                for j in range(n):
                    # counting the frequency of nums[i]
                    if nums[j] == nums[i]:
                        cnt += 1
                
                if cnt > (n // 3):
                    result.append(nums[i])
                
            if len(result) == 2:
                break
        
        return result
    
    def better_majorityElementTwo(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = []

        mpp = defaultdict(int)

        mini = n // 3 + 1

        for num in nums:
            mpp[num] += 1

            if mpp[num] == mini:
                result.append(num)

            if len(result) == 2:
                break

        return result
    

    def optimal_majorityElementTwo(self, nums: List[int]) -> List[int]:        
        n = len(nums)

        cnt1, cnt2 = 0, 0
        el1, el2 = nums[0], nums[0]
        for num in nums:
            if cnt1 == 0 and el2 != num:
                cnt1 = 1
                el1 = num 
            elif cnt2 == 0 and el1 != num:
                cnt2 = 1
                el2 = num 
            elif num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1 
            else:
                cnt1 -= 1 
                cnt2 -= 1

        cnt1, cnt2 = 0, 0 
        
        for num in nums:
            if num == el1:
                cnt1 += 1 
            if num == el2:
                cnt2 += 1

        mini = n // 3 + 1
        
        result = []

        if cnt1 >= mini:
            result.append(el1)
            
        if cnt2 >= mini and el1 != el2:
            result.append(el2)
        return result

arr = [11, 33, 33, 11, 33, 11]

sol = Solution()

ans = sol.optimal_majorityElementTwo(arr)

print("The majority elements are:", end=" ")
for it in ans:
    print(it, end=" ")
print()