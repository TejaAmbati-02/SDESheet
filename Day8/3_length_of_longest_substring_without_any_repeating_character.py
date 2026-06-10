class Solution:
    def longestNonRepeatingSubstring(self, s):
        n = len(s)        
        HashLen = 256
        hash = [-1] * HashLen
        for i in range(HashLen):
            hash[i] = -1
        l, r, maxLen = 0, 0, 0
        while r < n:
            if hash[ord(s[r])] != -1:
                l = max(hash[ord(s[r])] + 1, l)

            current_len = r - l + 1            
            maxLen = max(current_len, maxLen)
            hash[ord(s[r])] = r
            r += 1
        return maxLen

s = "cadbzabcd"

sol = Solution()

result = sol.longestNonRepeatingSubstring(s)

print(f"The maximum length is: {result}")

