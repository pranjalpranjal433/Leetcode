class Solution:
    def isPalindrome(self, s: str) -> bool:
        def pal(i,j):
            if i>=j:
                return True
            while (s[i].isalpha()==False and s[i].isdigit()==False) and i<j:
                i+=1
            while s[j].isalpha()==False and s[j].isdigit()==False and j>i:
                j-=1
            if s[i].lower()!=s[j].lower():
                return False
            return pal(i+1,j-1)
        return pal(0,len(s)-1)