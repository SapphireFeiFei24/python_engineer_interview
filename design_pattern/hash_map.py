class HashMap:
    def __init__(self):
        self.key_size = 2069
        self.hash_table = [[] for i in range(self.key_size)]

    def hash(self, key):
        return key % self.key_size
    def put(self, key, val):
        idx = self.hash(key)
        for i in range(len(self.hash_table[idx])):
            if self.hash_table[idx][i][0] == key:
                self.hash_table[idx][i][1] = val
                return
        self.hash_table[idx].append([key, val])

    def get(self, key):
        idx = self.hash(key)
        for i in range(len(self.hash_table[idx])):
            if self.hash_table[idx][i][0] == key:
                return self.hash_table[idx][i][1]
        return -1

    def remove(self, key):
        idx = self.hash(key)
        for i in range(len(self.hash_table[idx])):
            if self.hash_table[idx][i][0] == key:
                self.hash_table[idx].pop(i)
                break
if __name__ == "__main__":
    object = HashMap()
    object.put(1,1)
    print(object.get(1))