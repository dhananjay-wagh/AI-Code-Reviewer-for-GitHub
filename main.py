import os
import json

def processData(d):
    x = []
    for i in range(len(d)):
        if d[i] != None:
            x.append(d[i]*2)
    return x

def saveFile(data,filename):
    f = open(filename, 'w')
    json.dump(data,f)
    f.close()

def loadFile(filename):
    f = open(filename,'r')
    data = json.load(f)
    return data

def calculate(a,b,operation):
    if operation == 'add':
        result = a+b
    elif operation == 'subtract':
        result = a-b
    elif operation == 'divide':
        result = a/b
    return result

data = [1,2,None,4,5]
result = processData(data)
saveFile(result,'output.json')
print(calculate(10,0,'divide'))
