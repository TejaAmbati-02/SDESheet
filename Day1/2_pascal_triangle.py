# Brute force Approach
class Solution:
    def brute_force_pascal_triangle(self, row_nums):
        pascal_triangle = []

        for row in range(row_nums):
            rows = [1] * (row+1)
            for col in range(1, row):
                rows[col] = pascal_triangle[row-1][col-1] + pascal_triangle[row-1][col]
            pascal_triangle.append(rows)
        return pascal_triangle




    def better_approach_pascal_triangle(self, row_nums):
        row = []
        value = 1
        row.append(value)

        for k in range(1, row_nums):
            value = value * (row_nums - k) // k
            row.append(value)
        return row


    def optimal_approach_pascal_triangle(self, row_num, col_num):
        n = row_num - 1
        k = col_num - 1

        result = 1

        # Compute C(n, k) using iterative formula
        for i in range(k):
            result *= (n - i)
            result //= (i + 1)

        return result


obj = Solution()
n = 5

result = obj.brute_force_pascal_triangle(n)
for row in result:
    print(" ".join(map(str, row)))


result = obj.brute_force_pascal_triangle(n)
for row in result:
    print(" ".join(map(str, row)))

r, c = 5, 3
print(obj.optimal_approach_pascal_triangle(r, c))


