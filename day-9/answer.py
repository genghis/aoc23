from aocd import get_data
dataset = [[int(y) for y in x.split(' ')] for x in get_data(day=9, year=2023).splitlines()]

def sequencer(line, direction):
    if direction == 'back':
        line.reverse()
    counter = 0
    while line.count(0) != len(line):
        counter += line[-1]
        line = [b - a for a, b in zip(line[:-1], line[1:])]
    return counter

def first():
    results = []
    for i in dataset:
        results.append(sequencer(i, 'forward'))
    print(f"PART ONE: {sum(results)}")

def second():
    results = []
    for i in dataset:
        results.append(sequencer(i, 'back'))
    print(f"PART TWO: {sum(results)}")

if __name__ == "__main__":
    first()
    second()