class Solution:
    def isHappy(self, n: int) -> bool:
        l = set()
        while True:
            num = str(n)
            n = 0
            for i in range(0,len(num)):
                n += (int(num[i]) ** 2)
            if n == 1:
                return True
            if n in l:
                break
            l.add(n)
        return False