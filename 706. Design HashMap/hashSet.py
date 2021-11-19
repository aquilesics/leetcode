class MyHashSet:
    def __init__(self):
        self.hs = set()
    
    def add(self, key : int) -> None:
        self.hs.add(key)

    def remove(self, key) -> None:
        try :
            self.hs.remove(key)
        except:
            None

    def contains(self, key) -> bool:
        return key in self.hs



#Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(9)
obj.remove(9)
param_3 = obj.contains(9)
