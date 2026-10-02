class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = {} #create an empty directory
        for string in strs:  #Visit each word one by one.
            sorted_string = "".join(sorted(string))  #sorted("eat")  ['a', 'e', 't']  "".join(['a','e','t'])  "aet"
            if sorted_string in hashMap: #Check if "aet" already exists as a key.
                hashMap[sorted_string].append(string)
            else:
                hashMap[sorted_string] = [string]
        return list(hashMap.values())



