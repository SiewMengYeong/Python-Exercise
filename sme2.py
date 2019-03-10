def f(n):
    if n > 1:
        f(n // 2)
        print (n)

f(5)
