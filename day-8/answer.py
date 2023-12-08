from aocd import get_data
from math import lcm

directions,network = get_data(day=8, year=2023).split('\n\n')
network = network.splitlines()

def first():
    net = {}
    for i in network:
        key,data = i.split(' = ')
        tup = (data.split(',')[0][1::], data.split(', ')[1][:-1:])
        net[key] = tup
    count = 0
    total = 0
    current = 'AAA'
    while current != 'ZZZ':
        match directions[count]:
            case 'L':
                if count == len(directions)-1:
                    count = 0
                else:
                    count+=1
                current = net[current][0]
                total+=1
            case 'R':
                if count == len(directions)-1:
                    count = 0
                else:
                    count+=1
                current = net[current][1]
                total+=1
    print(total)

def second():
    net = {}
    for i in network:
        key,data = i.split(' = ')
        tup = (data.split(',')[0][1::], data.split(', ')[1][:-1:])
        net[key] = tup
    alist = ['AAA', 'HVA', 'HHA', 'BVA', 'RSA', 'NPA']
    results = []
    for i in alist:
        total = 0
        ct = 0
        current = i
        while current[-1] != 'Z':
            match directions[ct]:
                case 'L':
                    if ct == len(directions)-1:
                        ct = 0
                    else:
                        ct+=1
                    current = net[current][0]
                    total+=1
                case 'R':
                    if ct == len(directions)-1:
                        ct = 0
                    else:
                        ct+=1
                    current = net[current][1]
                    total+=1
        results.append(total)
    print(results)
    answer = 1
    for i in results:
        answer *= i
    print(lcm(*results))

if __name__ == "__main__":
    first()
    second()