import random
def problem1():
    count = 0
    l = [random.randint(0,99) for r in xrange(30)]
    for i in l:
        if i%2==0:
            count+=1
    return(count)
print(problem1())


def problem2():
    l = [random.randint(0,99) for r in xrange(30)]
    for i in l:
        if 


