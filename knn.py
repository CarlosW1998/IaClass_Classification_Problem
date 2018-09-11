from DataAcesses import Flower
class knn:
    def __init__(self, data, neighborhood):
        self.data = data
        self.neighborhood = neighborhood
    def dist(self, a, b):
        dist = 0
        dist += (a.sepallen - b.sepallen)**2
        dist += (a.sepalwidth - b.sepalwidth) ** 2
        dist += (a.petallen - b.petallen) ** 2
        dist += (a.petalwidht - b.petalwidht) ** 2
        dist = dist**(1/2)
        return dist

    def classify(self, case):
        neighboors = []
        for a in range(self.neighborhood):
            neighboors.append([self.dist(a, case), case]);




