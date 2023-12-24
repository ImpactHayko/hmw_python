def custom_zip(*iterables):
    minlen=min(len(i) for i in iterables)
    res = []
    for j in range(minlen):
        res.append(tuple(i[j] for i in iterables))
    return res

ls = [1,2]
ls1 = [3,4]
ls2 = ['a','b','c','d']

print(list(custom_zip(ls, ls1, ls2)))
