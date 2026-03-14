class HitCounter:
    def __init__(self):
        self.hits = []
        self.count = 0

    def hit(self, timestamp):
        while self.hits and timestamp - self.hits[0][0] >= 300:
            self.count -= self.hits.pop(0)[1]
        if timestamp == self.hits[-1][0]:
            self.hits[-1][1] += 1
        else:
            self.hits.append(1)

    def getHits(self, timestamp):
        while self.hits and timestamp - self.hits[0][0] >= 300:
            self.count -= self.hits.pop(0)[1]
        return self.count