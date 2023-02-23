for i in range(1, 10):
    for j in range(1, 10):
        print(i, "×", j, "=", i*j)

for i in range(1, 10):
    k = ""
    for j in range(1, 10):
        k += "{}x{}={:2d} ".format(i,j,i*j)
    print(k)
