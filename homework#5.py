import random
def gen(n, x, y):
    l = [random.randint(x,y) for r in range(n)]
    return l

def find(l, sum):
    print(l)
    result = []
    for i in range(len(l) - 1):
        for q in range(i, len(l) - 1):
            if l[i] + l[q + 1] == sum:
                result.append(l[i])
                result.append(l[q + 1])
    return result

print(find(gen(10,0,9), 10))






