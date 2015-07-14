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
    minnum = 100.00
    maxnum = 1
    for i in l:
        if i < minnum:
            minnum = i
        elif i > maxnum:
            maxnum = i
    return maxnum-minnum
print(problem2())

def problem3(str):
    return str.lower().count('qa')
print(problem3('fwerfgwfqawefwQafgeQfwefaqfeqkjfnQAfkklqA'))

def problem3a(str, substring):
    count = 0
    strlow = str.lower()
    for i in range(0,(len(str))):
        if strlow[i:i+len(substring)] == substring:
            count+=1
    return count
print(problem3a('fwerfgwfqawefwQafgeQfwefaqfeqkjfnQAfkklqA', 'qa'))

def homework():
    l = [random.randint(0,99) for r in xrange(200)]
    indices = []
    print(l)
    while True:
        try:
            x = int(raw_input('Please enter number: '))
        except ValueError:
            print('Not an Integer')
            break
        else:
            if 0 <= int(x) <= 99:
                if x in l:
                    indices = [i for i,val in enumerate(l) if val==x]
                    print(indices)
                else:
                    print('Not found')
            else:
                print('Out of range')
        break

homework()