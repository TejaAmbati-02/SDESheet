class Solution:
    def brute_force_sortZeroOneTwo(self, nums):
        count0 = count1 = count2 = 0

        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        index = 0

        for i in range(count0):
            nums[index] = 0
            index += 1

        for i in range(count1):
            nums[index] = 1
            index += 1

        for i in range(count2):
            nums[index] = 2
            index += 1

    def better_sortZeroOneTwo(self, nums):
        cnt0 = cnt1 = cnt2 = 0

        for num in nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
            else:
                cnt2 += 1


        for i in range(cnt0):
            nums[i] = 0

        for i in range(cnt0, cnt0 + cnt1):
            nums[i] = 1

        for i in range(cnt0 + cnt1, len(nums)):
            nums[i] = 2


    def optimal_sortZeroOneTwo(self, nums):
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


nums = [1, 0, 2, 1, 0]
obj = Solution()
obj.brute_force_sortZeroOneTwo(nums)
print(nums)

nums = [1, 0, 2, 1, 0]
obj.better_sortZeroOneTwo(nums)
print(nums)


nums = [1, 0, 2, 1, 0]
obj.optimal_sortZeroOneTwo(nums)
print(nums)