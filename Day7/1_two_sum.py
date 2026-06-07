class Solution:
    def two_sum_exists(self, arr, target):
        nums_with_index = [(num, idx) for idx, num in enumerate(arr)]
        
        nums_with_index.sort(key=lambda x: x[0])

        left, right = 0, len(arr) - 1
        
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            
            if current_sum == target:
                return "YES"
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return "NO"

    def two_sum_indices(self, arr, target):
        nums_with_index = [(num, idx) for idx, num in enumerate(arr)]
        
        nums_with_index.sort(key=lambda x: x[0])

        left, right = 0, len(arr) - 1
        
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if current_sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return [-1, -1]


sol = Solution()
arr = [2, 6, 5, 8, 11]
target = 14

print(sol.two_sum_exists(arr, target))
print(sol.two_sum_indices(arr, target))
