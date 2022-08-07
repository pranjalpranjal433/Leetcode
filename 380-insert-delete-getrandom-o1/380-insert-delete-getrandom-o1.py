from random import randint
class RandomizedSet:

    def __init__(self):
        self.a={}
        self.arr=[]
        self.l=0

    def insert(self, val: int) -> bool:
        if val in self.a:
            return False
        self.a[val]=self.l
        self.arr.append(val)
        self.l+=1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.a:
            return False
        if self.a[val]!=self.l-1:
            self.arr[self.a[val]]=self.arr[self.l-1]
            self.a[self.arr[self.l-1]]=self.a[val]
        del self.a[val]
        self.l-=1
        self.arr.pop()
        return True
    def getRandom(self) -> int:
        return self.arr[randint(0,self.l-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()