class knn:
    def __init__(self, data, nsize):
        self.data = data
        self.nsize = nsize;
    def dist(self, n1, n2):
        dist = 0;
        for a in range(len(n1)):
            dist += (n1[a]-n2[a])**2
        dist = dist**(1/2)
        return dist

    def classify(self, case):
        neighboors = []
        for a in self.data:
            neighboors.append([self.dist(case, a['Data']), a['Type']])
        counter = {}
        neighboors.sort()

        for a in neighboors[:self.nsize]:
            if a[1] not in counter.keys():
                counter[a[1]] = 0;
            counter[a[1]] += 1
        key = ''
        i = float('inf')
        for a in counter.keys():
            if counter[a] < i :
                i = counter[a]
                key = a;
        return key






