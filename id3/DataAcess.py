class Database:
    def __init__(self):
        self.file = open("Database.txt", "r")

    def selectAll(self):
        data = []
        for a in self.file.readlines():
            i = a.split(',')
            i[0], i[1], i[2], i[3] = float(i[0]), float(i[1]), float(i[2]), float(i[3])
            data.append({"SL": i[0], "SW": i[1], "PL": i[2], "PW": i[3], "Type": i[4].replace('\n', '')})
        return data

    def getMeans(self):
        return {"SL": 5.84, "SW": 3.05, "PL": 3.76, "PW": 1.20}
