myDict = {1: 'Easy', 2: 'Difficult'}

for key, value in myDict.items():
    print("{}: {}".format(key, value))

list(myDict.keys())



'_'.join(x + ': ' + y for x, y in myDict.items())

print('(' + ', '.join('{}: {}'.format(k,v) for k,v in myDict.items()) + ')')