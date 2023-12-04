from aocd import get_data
dataset = get_data(day=4, year=2023).splitlines()
def first():
    total = []
    for card in dataset:
        j = card.split(": ")
        winners, mine = j[1].split(" | ")
        winnerlist = [int(x) for x in winners.split(" ") if x]
        minelist = [int(x) for x in mine.split(" ") if x]
        results = [x for x in winnerlist if x in minelist]
        if results:
            counter = 1
        else:
            counter = 0
        for i in range(len(results)-1):
            counter *= 2
        total.append(counter)
    print(f"FIRST: {sum(total)}")


def second():
    cardnumbers = {k: 1 for (k,v) in enumerate(dataset)}
    for idx, card in enumerate(dataset):
        j = card.split(": ")
        winners, mine = j[1].split(" | ")
        winnerlist = [int(x) for x in winners.split(" ") if x]
        minelist = [int(x) for x in mine.split(" ") if x]
        results = [x for x in winnerlist if x in minelist]
        counter = 0
        for i in range(len(results)):
            counter += 1
        for i in range(cardnumbers[idx]):
            for j in range(1, counter+1):
                cardnumbers[idx+j] += 1
    print(f"SECOND: {sum(cardnumbers.values())}")

if __name__ == "__main__":
    first()
    second()