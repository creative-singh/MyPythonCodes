# Write a Python program to combine two dictionary adding values for common keys.
'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
mydic = {}
for key in d1:
    for keyd in d2:
        if key == keyd:
            sum1 = d1.get(key)
            sum2 = d2.get(keyd)
            tsum = sum1 + sum2
            mydic[key] = tsum
        if keyd not in mydic:
            mydic[keyd] = d2.get(keyd)
    if key not in mydic:
        mydic[key] = d1.get(key)
print(mydic)