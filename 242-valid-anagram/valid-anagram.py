class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}

        #count the characters in t
        for x in t:  #t =  n a g r a m
            if x in hashMap: # n in hash map current n is not there hashMap[x] = 1  Next: x = 'a'  a is not there. hashMap['a'] = 1 {'n': 1, 'a': 1}
                hashMap[x] = hashMap[x] + 1 # Next: x = 'a' again So this condition is true: and if x in hashMap:  hashMap[x] = hashMap[x] + 1  {'n': 1, 'a': 2, 'g': 1}
                
            else:
                hashMap[x] = 1
        # subtract character using s
        for x in s:
            if x in hashMap:
                hashMap[x] = hashMap[x] -1
            else:
                return False
        #check wheaterh all counts are 0 are not
        for x in hashMap:
            if hashMap[x] != 0:
                return False
        return True
















#         s = list(s)
#         t = list(t)
#         if len(s) != len(t):
#             return False
#         for i in range(len(s)):
#             flag = 0
#             for j in range(len(t)):
#                 if s[i] == t[j]:
#                     flag = 1
#                     break
#             if flag == 0:
#                 return False
#         return True
        