from knn import *
from DataAcesses import *
from CrossValidation import crossValidation
i = Database()
dados = i.selectAll()
for a in range(2, 120):
    print(str(a) + ' : ' + str(crossValidation(dados, a)))