class Database:
    def __init__(self):
        self.file = open("Database.txt", "r");
    def selectAll(self):
        data = []
        for a in self.file.readlines():
            data.append(Flower(list(a.split(','))))
        return data


class Flower:
    def __init__(self, s):
        self.sepallen = float(s[0])
        self.sepalwidth = float(s[1])
        self.petallen = float(s[2])
        self.petalwidht = float(s[3])
        self.type = s[4]
    def __str__(self):
        return  ("Sepal length: " + str(self.sepallen) + " cm\n" + "Sepal width: " + str(self.sepalwidth) + " cm\n" + "Petal length: " + str(self.petallen) +" cm\n" + "Petal width: " + str(self.petalwidht) + "Type: " + str(self.type))