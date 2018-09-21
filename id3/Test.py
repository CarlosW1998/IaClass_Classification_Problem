from id3.DataAcess import Database
from id3.ID3 import ID3, Tree

i = ID3()
d = Database()
j = d.selectAll()
case = j.pop(0)
i.train(j, d.getMeans())

a = i.classify(case)
print(a, case['Type'])
