terms = set()
start = 2
finish = 101
for i in range(start,finish):
    for j in range(start, finish):
        terms.add(pow(i,j))
print(terms.__len__())