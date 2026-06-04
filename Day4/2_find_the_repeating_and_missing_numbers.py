class Solution:
    def bruteforce_findMissingRepeatingNumbers(self, nums):
        
        n = len(nums) 
        repeating, missing = -1, -1

        for i in range(1, n + 1):
            cnt = nums.count(i)

            if cnt == 2:
                repeating = i
            elif cnt == 0:
                missing = i

            if repeating != -1 and missing != -1:
                break

        return [repeating, missing]

    def better_findMissingRepeatingNumbers(self, nums):        
        n = len(nums)
        
        hash = [0] * (n + 1)
        
        for num in nums:
            hash[num] += 1

        repeating = -1
        missing = -1
        
        for i in range(1, n + 1):
            if hash[i] == 2:
                repeating = i
            elif hash[i] == 0:
                missing = i

            if repeating != -1 and missing != -1:
                break
        

        return [repeating, missing]

    def optimal_findMissingRepeatingNumbers(self, nums):        
        n = len(nums)
        SN = (n * (n + 1)) // 2
        S2N = (n * (n + 1) * (2 * n + 1)) // 6
        S = 0
        S2 = 0
        for num in nums:
            S += num
            S2 += num * num

        val1 = S - SN
        val2 = S2 - S2N

        val2 = val2 // val1

        x = (val1 + val2) // 2
        y = x - val1

        return [int(x), int(y)]

    def optimal1_findMissingRepeatingNumbers(self, nums):        
        n = len(nums)

        xr = 0

        for i in range(n):
            xr = xr ^ nums[i] 
            
            xr = xr ^ (i + 1)  

        number = (xr & ~(xr - 1))

        zero = 0        
        one = 0  

        for i in range(n):
            if (nums[i] & number) != 0:
                
                one = one ^ nums[i]
                
            else:
                zero = zero ^ nums[i]

        for i in range(1, n + 1):
            
            if (i & number) != 0:
                one = one ^ i
                
            else:
                zero = zero ^ i

        cnt = 0

        for i in range(n):
            if nums[i] == zero:
                cnt += 1

        if cnt == 2:
            return [zero, one]

        return [one, zero]



nums = [3, 1, 2, 5, 4, 6, 7, 5]

sol = Solution()

result = sol.bruteforce_findMissingRepeatingNumbers(nums)
print(f"The repeating and missing numbers are: {{{result[0]}, {result[1]}}}")

result = sol.better_findMissingRepeatingNumbers(nums)
print(f"The repeating and missing numbers are: {{{result[0]}, {result[1]}}}")

result = sol.optimal_findMissingRepeatingNumbers(nums)
print(f"The repeating and missing numbers are: {{{result[0]}, {result[1]}}}")

result = sol.optimal1_findMissingRepeatingNumbers(nums)
print(f"The repeating and missing numbers are: {{{result[0]}, {result[1]}}}")