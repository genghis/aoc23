from aocd import get_data
dataset = get_data(day=6, year=2023).splitlines()

time = [int(x) for x in dataset[0].split(" ") if x.isnumeric()]
distance = [int(x) for x in dataset[1].split(" ") if x.isnumeric()]
pairs = [(x, y) for x,y in zip(time,distance)]
secondtime = [x for x in dataset[0].split(" ") if x.isnumeric()]
seconddistance = [x for x in dataset[1].split(" ") if x.isnumeric()]
time2 = int(''.join(secondtime))
distance2 = int(''.join(seconddistance))

def first():
    totalwins = 1
    for pair in pairs:
        wins = 0
        for n in range(pair[0]):
            hold = pair[0]-n
            if (hold * (pair[0]-hold)) > pair[1]:
                wins += 1
        print(wins)
        totalwins *= wins
    print(totalwins)

def second():
    wins = 0
    for n in range(time2):
        hold = time2-n
        if (hold * (time2-hold)) > distance2:
            wins += 1
    print(wins)

if __name__ == "__main__":
    first()
    second()