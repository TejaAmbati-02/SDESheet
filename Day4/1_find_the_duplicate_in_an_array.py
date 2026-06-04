class Solution:
    def bruteforce_findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1


    def better_find_duplicate(self, arr: list[int]) -> int:
        n = len(arr)
        freq = [0] * (n + 1)
        for x in arr:
            if freq[x] == 0:
                freq[x] += 1
            else:
                return x
        return 0


    def optimal_find_duplicate(self, nums: list[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow



sol = Solution()
arr = [1, 3, 4, 2, 2]
print("The duplicate element is " + str(sol.bruteforce_findDuplicate(arr)))
print("The duplicate element is " + str(sol.better_find_duplicate(arr)))
print("The duplicate element is " + str(sol.optimal_find_duplicate(arr)))