class MyHashSet:
    mylist = []
    def __init__(self):
        self.mylist = []

    def add(self, key: int) -> None:
        self.mylist.append(key)

    def remove(self, key: int) -> None:
        self.mylist = [e for e in self.mylist if e != key]

    def contains(self, key: int) -> bool:
        return key in self.mylist