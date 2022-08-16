from random import randint

class RandomizedCollection:

    def __init__(self):
        self.a=defaultdict(set)
        self.arr=[]
        self.l=0

    def insert(self, val: int) -> bool:
        self.a[val].add(self.l)
        self.arr.append(val)
        self.l+=1
        return len(self.a[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.a[val]:
            return False
        ind, last = self.a[val].pop(), self.arr[-1]
        self.arr[ind]=last
        self.a[last].add(ind)
        self.a[last].discard(self.l-1);
        self.l-=1
        self.arr.pop()
        return True
    def getRandom(self) -> int:
        return self.arr[randint(0,self.l-1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()