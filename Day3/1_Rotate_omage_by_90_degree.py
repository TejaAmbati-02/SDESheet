class Solution:
    def bruteforce_rotateClockwise(self, matrix):
        n = len(matrix)

        rotated = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated[j][n - i - 1] = matrix[i][j]

        return rotated
    
    def optimal_rotateClockwise(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

obj = Solution()
rotated = obj.bruteforce_rotateClockwise(matrix)

for row in rotated:
    print(*row)


print("="*20)

rotated = obj.optimal_rotateClockwise(matrix)

for row in matrix:
    print(*row)
