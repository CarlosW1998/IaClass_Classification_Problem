from math import *

class Tree:
    def __init__(self, type, division):
        self.type = type
        self.division = division
        self.descendents = {'left': None, 'right': None}

    def __str__(self):
        return (str(self.type) + ' ' + str(self.division))

    def addLeft(self, d):
        self.descendents['left'] = d

    def addRight(self, d):
        self.descendents['right'] = d

    def getLeft(self):
        return self.descendents['left']

    def getRight(self):
        return self.descendents['right']

class ID3:
    def entropy(self, set, max):
        result = 0;
        for i in set.keys():
            if set[i] != 0:
                result -= (set[i]/max)*log(set[i]/max, 2)
        return result

    def gain(self, set, max, entropy):
        result = entropy
        for i in set:
            result -= (i[0]/max)*i[1]
        return result

    def format(self, data):
        form = {}
        for i in data:
            if i["Type"] not in form.keys():
                form[i['Type']] = 0
            form[i['Type']] += 1
        return form

    def max(self, data):
        result = data[0]
        for i in data:
            if i[0] > result[0]:
                result = i
        return result

    def train(self, data, rules):
        self.DTree = self.getTree(data, rules)

    def getTree(self, data, rules):
        mygain = []
        if(len(data) == 0 or len(rules) == 0): return None

        for i in rules.keys():
            d1 = []
            d2 = []
            entropys = []

            for j in data:
                if j[i] > rules[i]: d1.append(j)
                else : d2.append(j)

            e = self.entropy(self.format(d1), len(d1))
            entropys.append([len(d1), e])
            e = self.entropy(self.format(d2), len(d2))
            entropys.append([len(d2), e])

            mygain.append([self.gain(entropys, len(data), self.entropy(self.format(data), len(data))), i, d2, d1])

        maxGain = self.max(mygain)
        if maxGain[0] <= 0: return  None
        myTree = Tree(maxGain[1], rules[maxGain[1]])
        del rules[maxGain[1]]
        newrules1 = {}
        newrules2 = {}
        for i in rules.keys():
            newrules1[i] = rules[i]
            newrules2[i] = rules[i]

        myTree.addLeft(self.getTree(maxGain[2], newrules1))
        if myTree.getLeft() == None:
            finaldata = self.format(maxGain[2])
            result = ['nada', -float('inf')]
            for i in finaldata.keys():
                if finaldata[i] > result[1]:
                    result = [i, finaldata[i]]
            myTree.addLeft(result[0])

        myTree.addRight(self.getTree(maxGain[3], newrules2))
        if myTree.getRight() == None:
            finaldata = self.format(maxGain[3])
            result = ['nada', -float('inf')]
            for i in finaldata.keys():
                if finaldata[i] > result[1]:
                    result = [i, finaldata[i]]
            myTree.addRight(result[0])
        return myTree

    def classify(self, data):
        i = self.DTree
        while type(i) != type(''):
            if data[i.type] > i.division: i = i.getRight()
            else: i = i.getLeft()
        return i