from itertools import permutations

class Solution:
    def brute_force_next_permutation(self, row_nums):
        perms = sorted(set(permutations(row_nums)))

        current = tuple(row_nums)

        for i in range(len(perms)):
            if perms[i] == current:
                if i == len(perms) - 1:
                    return list(perms[0])
                return list(perms[i + 1])

        return row_nums




    def optimal_next_permutation(self, nums):
        index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        if index == -1:
            nums.reverse()
            return

        for i in range(len(nums) - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        nums[index + 1:] = reversed(nums[index + 1:])


sol = Solution()
nums = [1, 2, 3]
result = sol.brute_force_next_permutation(nums)
print(" ".join(map(str, result)))


nums = [1, 2, 3]
sol = Solution()
sol.optimal_next_permutation(nums)
print(" ".join(map(str, nums)))

