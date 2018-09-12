from knn import *
from DataAcesses import *
from CrossValidation import crossValidation

i = Database()
dados = i.selectAll()
crossValidation(dados, 2)