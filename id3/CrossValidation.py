from id3.ID3 import *

def crossValidation(data, rules):
    ac = 0
    confusion = {}
    for i in range(len(data)):
        currentrules = {}
        for i in rules.keys():
            currentrules[i] = rules[i]
        case = data.pop(0)
        i = ID3()
        i.train(data, currentrules)
        result = i.classify(case)
        if result == case['Type']:
            ac += 1

        if case['Type'] not in confusion.keys():
            confusion[case['Type']] = {}
        if result not in confusion[case['Type']].keys():
            confusion[case['Type']][result] = 0
        confusion[case['Type']][result] += 1
        data.append(case)
    ac /= len(data)
    print("Acuracia: " + str(ac * 100) + "%")
    for i in confusion.keys():
        print(i, end='')
        print(confusion[i])