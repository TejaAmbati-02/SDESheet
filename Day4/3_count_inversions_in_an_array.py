class Solution:

    def bruteforce_number_of_inversions(self, arr):
        cnt = 0
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] > arr[j]:
                    cnt += 1
        return cnt



    def _merge(self, arr, low, mid, high):
        temp = []

        left = low
        right = mid + 1

        cnt = 0

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                cnt += (mid - left + 1)
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return cnt

    def _mergeSort(self, arr, low, high):
        cnt = 0

        if low >= high:
            return cnt

        mid = (low + high) // 2

        cnt += self._mergeSort(arr, low, mid)
        cnt += self._mergeSort(arr, mid + 1, high)
        cnt += self._merge(arr, low, mid, high)

        return cnt

    def optimal_numberOfInversions(self, arr):
        return self._mergeSort(arr, 0, len(arr) - 1)

sol = Solution()
arr = [5, 4, 3, 2, 1]
inversions = sol.bruteforce_number_of_inversions(arr)
print("The number of inversions is:", inversions)

arr = [5, 4, 3, 2, 1]
inversions = sol.optimal_numberOfInversions(arr)
print("The number of inversions is:", inversions)
