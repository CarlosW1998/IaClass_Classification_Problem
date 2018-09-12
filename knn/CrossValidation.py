from knn import  *

def crossValidation(data, n):
    ac = 0
    confusion = {}
    for a in range(len(data)):
        test = data.pop(0)
        model = knn(data, n)
        result = model.classify(test['Data'])
        if(result == test['Type']):
            ac+=1
        if test['Type'] not in confusion.keys():
            confusion[test['Type']] = {}
        if result not in confusion[test['Type']].keys():
            confusion[test['Type']][result] = 0
        confusion[test['Type']][result] += 1
        data.append(test)
        confusion.keys()
    ac /= len(data)
    print("Acuracia: " + str(ac*100) + "%")
    for i in confusion.keys():
        print(i, end = '')
        print(confusion[i])
