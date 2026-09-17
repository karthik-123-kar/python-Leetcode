# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i in range(len(s)):
#             count = 0
#             for j in range(len(s)):
#                 if s[i] == s[j]:
#                     count += 1
#             if count == 1:
#                 return i
#         return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1
        