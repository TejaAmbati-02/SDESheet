class Solution:
    def brute_force_stockbuySell(self, prices):
        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit, profit)

        return maxProfit

    def optimal_stockbuySell(self, prices):
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print("Max Profit:", sol.brute_force_stockbuySell(prices))
print("Max Profit:", sol.optimal_stockbuySell(prices))
