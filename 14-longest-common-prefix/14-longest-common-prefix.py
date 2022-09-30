class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        a=''
        s1=strs[0]
        s2=strs[len(strs)-1]
        for i in range(min(len(strs[0]),len(strs[len(strs)-1]))):
            if s1[i]==s2[i]:
                a+=s1[i]
            else:
                break
        return a