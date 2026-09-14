class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix
