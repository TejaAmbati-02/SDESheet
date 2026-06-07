class Solution:
    def longestConsecutive(self, nums):
        n = len(nums)
        if n == 0:
            return 0 

        longest = 1 
        st = set()

        for i in range(n):
            st.add(nums[i])

        for it in st:
            if it - 1 not in st:
                cnt = 1 
                x = it 

                while x + 1 in st:
                    x = x + 1 
                    cnt = cnt + 1 
                longest = max(longest, cnt)
        return longest

a = [100, 4, 200, 1, 3, 2] 
solution = Solution() 
ans = solution.longestConsecutive(a) 
print("The longest consecutive sequence is", ans)
