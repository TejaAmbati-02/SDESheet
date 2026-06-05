class Solution:
    def bruteforce_myPow(self, x, n):
        if n == 0 or x == 1.0:
            return 1
        
        temp = n
        
        if n < 0:
            x = 1 / x
            temp = -1 * n

        ans = 1

        for i in range(temp):
            ans *= x 
        return ans

    def _power(self, x, n):
        if n == 0:
            return 1.0
        
        if n == 1:
            return x
        
        if n % 2 == 0:
            return self._power(x * x, n // 2)
        
        return x * self._power(x, n - 1)

    def optimal_myPow(self, x, n):
        if n < 0:
            return 1.0 / self._power(x, -n)
        
        return self._power(x, n)


sol = Solution()
print(f"{sol.bruteforce_myPow(2.0000, 10):.4f}")
print(f"{sol.optimal_myPow(2.0, 10):.4f}")



