from id3.DataAcess import *
from id3.CrossValidation import *

mydata = Database()

crossValidation(mydata.selectAll(), mydata.getMeans())