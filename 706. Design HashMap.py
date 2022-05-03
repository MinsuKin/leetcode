class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        bucket, index = self.getIndex(key)
        if index < 0:
            bucket.append((key,value))
        else:
            bucket[index] = (key, value)
            
    def get(self, key: int) -> int:
        bucket, index = self.getIndex(key)
        if index < 0:
            return -1
        else:
            return bucket[index][1]

    def remove(self, key: int) -> None:
        bucket, index = self.getIndex(key)
        if index < 0:
            return
        else:
            bucket.remove(bucket[index])
            
    def hashKey(self, key):
        return key % self.size
    
    def getIndex(self, key):
        hashResult = self.hashKey(key)
        bucket = self.buckets[hashResult]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                return bucket, i
        
        return bucket, -1


# class MyHashMap:
#     def __init__(self):
#         self.l = [-1 for _ in range(1000001)]
        
#     def put(self, key: int, value: int) -> None:
#         self.l[key] = value
        
#     def get(self, key: int) -> int:
#         return self.l[key]
    
#     def remove(self, key: int) -> None:
#         self.l[key] = -1
        