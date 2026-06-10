class Solution:
    def maxLen(self, nums: list[int], n: int) -> int:
        mpp: dict[int, int] = {}
        maxi = 0
        s = 0

        for i in range(n):
            s += nums[i]

            if s == 0:
                maxi = i + 1
            else:
                if s in mpp:
                    maxi = max(maxi, i - mpp[s])
                else:
                    mpp[s] = i

        return maxi

nums = [9, -3, 3, -1, 6, -5]
n = len(nums)
solution = Solution()
print(solution.maxLen(nums, n))
