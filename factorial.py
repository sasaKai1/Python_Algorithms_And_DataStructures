def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

for i in range(0, 21):
    print("{}!=".format(i), fact(i))
