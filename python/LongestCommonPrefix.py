class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix =  ""

        for i in range(len(strs[0])):
            currPrefix = longestPrefix + strs[0][i]
            startsWith = True
            for word in strs:
                startsWith = word.startswith(currPrefix)
                if not startsWith: 
                    break
            if startsWith:
                longestPrefix = currPrefix

        return longestPrefix