# from aocd import get_data
from operator import itemgetter

dataset = open('input.txt').read().splitlines()
print(dataset)

# dataset = get_data(day=7, year=2023)
# dataset = '''32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483'''.splitlines()

# dataset2 = [(list(x.split(' ')[0]), int(x.split(' ')[1])) for x in dataset]

# dataset2 = list(map(lambda x: x[0].replace('A', '14'), dataset2))
# dataset2 = list(map(lambda x: x[0].replace('K', '13'), dataset2))
# dataset2 = list(map(lambda x: x[0].replace('Q', '12'), dataset2))
# dataset2 = list(map(lambda x: x[0].replace('J', '11'), dataset2))
# dataset2 = list(map(lambda x: x[0].replace('T', '10'), dataset2))
# print(dataset2)
hands = {
    "fivekind": {"rank": 1, "hands": []},
    "fourkind": {"rank": 2, "hands": []},
    "fullhouse": {"rank": 3, "hands": []},
    "threekind": {"rank": 4, "hands": []},
    "twopair": {"rank": 5, "hands": []},
    "onepair": {"rank": 6, "hands": []},
    "highcard": {"rank": 7, "hands": []}
}

payout = []

def rank_hands():
    ranks = len(dataset)
    # print(hands['fivekind']['hands'])
    for i in sorted(hands['fivekind']['hands'], key=itemgetter(0,1,2,3,4), reverse=True):
        payout.append(ranks*i[-1])
        print(f"Draw: Fivekind, Hand: {i}, Rank: {ranks}")
        ranks -= 1
    for i in sorted(hands['fourkind']['hands'], key=itemgetter(0,1,2,3,4), reverse=True):
        payout.append(ranks*i[-1])
        print(f"Draw: Fourkind, Hand: {i}, Rank: {ranks}")
        ranks -= 1
    for i in sorted(hands['fullhouse']['hands'], key=itemgetter(0,1,2,3,4), reverse=True):
        payout.append(ranks*i[-1])
        print(f"Draw: Fullhouse, Hand: {i}, Rank: {ranks}")
        ranks -= 1
    for i in sorted(hands['threekind']['hands'], key=itemgetter(0,1,2,3,4), reverse=True):
        payout.append(ranks*i[-1])
        print(f"Draw: Threekind, Hand: {i}, Rank: {ranks}")
        ranks -= 1
    for i in sorted(hands['twopair']['hands'], key=itemgetter(0,1,2,3,4), reverse=True):
        payout.append(ranks*i[-1])
        print(f"Draw: Twopair, Hand: {i}, Rank: {ranks}")
        ranks -= 1
    for i in sorted(hands['onepair']['hands'], key=itemgetter(0,1,2,3,4), reverse=True):
        payout.append(ranks*i[-1])
        print(f"Draw: Onepair, Hand: {i}, Rank: {ranks}")
        ranks -= 1
    for i in sorted(hands['highcard']['hands'], key=itemgetter(0,1,2,3,4), reverse=True):
        payout.append(ranks*i[-1])
        print(f"Draw: Highcard, Hand: {i}, Rank: {ranks}")
        ranks -= 1
    return sum(payout)
    
    
def first():
    for i in dataset:
        hand, bid = i.split(' ')
        bid = int(bid)
        handlist = []
        for char in hand:
            match char:
                case 'T':
                    handlist.append(10)
                case 'J':
                    handlist.append(11)
                case 'Q':
                    handlist.append(12)
                case 'K':
                    handlist.append(13)
                case 'A':
                    handlist.append(14)
                case _:
                    handlist.append(int(char))
        handlist.append(bid)
        # print(handlist)
        # print(hand)
        # print(set(handlist[0:5]))
        # print(len(set(handlist[0:5])))
        match len(set(handlist[0:5])):
            case 1:
                hands['fivekind']['hands'].append(handlist)
            case 2:
                decide = []
                for j in set(handlist[0:5]):
                    decide.append(handlist.count(j))
                if 4 in decide:
                    hands['fourkind']['hands'].append(handlist)
                else:
                    hands['fullhouse']['hands'].append(handlist)
            case 3:
                decide = []
                for j in set(handlist[0:5]):
                    decide.append(handlist.count(j))
                if 2 in decide:
                    hands['twopair']['hands'].append(handlist)
                else:
                    hands['threekind']['hands'].append(handlist)
            case 4:
                hands['onepair']['hands'].append(handlist)
            case 5:
                hands['highcard']['hands'].append(handlist)
    # print(hands['onepair']['hands'])
    print(rank_hands())
    

def second():
    pass

if __name__ == "__main__":
    first()
    second()