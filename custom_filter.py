def custom_filter(func, iterable):

    if func is None:
        res = [i for i in iterable if bool(i) == True]

        return res

    else:
        res = [i for i in iterable if func(i) == True]

    return res

ls = [1, 2, 3, [], 4, 5]

result1 = custom_filter(None, ls)

print(result1)


def foo(x):
    if isinstance(x, int):
        return x % 2 == 0

result2 = custom_filter(foo, ls)

print(result2)
