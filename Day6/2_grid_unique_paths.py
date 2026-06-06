class Solution:
    def func(self, m, n):
        prev = [0] * n
        for i in range(m):
            temp = [0] * n
            
            for j in range(n):
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue
                up = prev[j] if i > 0 else 0
                left = temp[j - 1] if j > 0 else 0
                temp[j] = up + left
            
            prev = temp
        return prev[-1]

    def uniquePaths(self, m, n):
        return self.func(m, n)

m = 3
n = 2

sol = Solution()

print("Number of ways:", sol.uniquePaths(m, n))