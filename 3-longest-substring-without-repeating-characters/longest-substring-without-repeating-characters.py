class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            current = ""
            for j in range(i,len(s)):
                if s[j] in current:
                    break
                current += s[j]
                if len(current) > max_len:
                    max_len = len(current)
        return max_len
