def foo(x, y):
    return x + y

ls1 = [1, 2, 3]
ls2 = [4, 5]

def custom_map(func, *iterable):
    min_lenght = min([len(x) for x in iterable])

    res = [foo(*[iterable [j][i] for j in range(len(iterable))]) for i in range(min_lenght)]

    return res

x = tuple(custom_map(foo, ls1, ls2))

print(x)
