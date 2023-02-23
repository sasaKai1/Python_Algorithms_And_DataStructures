
def add(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def add_2(n):
    total = (1+n)*n/2
    return int(total)

print(add(10))
print(add_2(10))
