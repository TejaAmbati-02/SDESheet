class Solution:
    def bruteforce_searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True

        return False


    def _binarySearch(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            elif target > nums[mid]:
                low = mid + 1

            else:
                high = mid - 1

        return False

    def better_searchMatrix(self, matrix, target):
        n = len(matrix)

        m = len(matrix[0])

        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m - 1]:
                return self._binarySearch(matrix[i], target)

        return False


    def optimal_searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])

        low = 0
        high = n * m - 1

        while low <= high:
            mid = (low + high) // 2

            row = mid // m
            col = mid % m

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

obj = Solution()

print("true") if obj.bruteforce_searchMatrix(matrix, 8) else print("false")

print("true") if obj.better_searchMatrix(matrix, 8) else print("false")

print("true") if obj.optimal_searchMatrix(matrix, 8) else print("false")
