from aocd import get_data
from operator import itemgetter

dataset = get_data(day=7, year=2023).splitlines()

hands = {
    "fivekind": [],
    "fourkind": [],
    "fullhouse": [],
    "threekind": [],
    "twopair": [],
    "onepair": [],
    "highcard": []
}

bids = {}

def rank_hands():
    score = 0
    ranks = len(dataset)
    for i in sorted(hands['fivekind'], key=itemgetter(0,1,2,3,4), reverse=True):
        score+=(ranks*i[-1])
        print(f"Draw: Fivekind, Hand: {i}, Bid: {i[-1]}, Rank: {ranks}")
        ranks -= 1
    for i in sorted(hands['fourkind'], key=itemgetter(0,1,2,3,4), reverse=True):
        score+=(ranks*i[-1])
        print(f"Draw: Fourkind, Hand: {i}, Bid: {i[-1]}, Rank: {ranks}")
        ranks -= 1
    for i in sorted(hands['fullhouse'], key=itemgetter(0,1,2,3,4), reverse=True):
        score+=(ranks*i[-1])
        print(f"Draw: Fullhouse, Hand: {i}, Bid: {i[-1]}, Rank: {ranks}")
        ranks -= 1
    for i in sorted(hands['threekind'], key=itemgetter(0,1,2,3,4), reverse=True):
        score+=(ranks*i[-1])
        print(f"Draw: Threekind, Hand: {i}, Bid: {i[-1]}, Rank: {ranks}")
        ranks -= 1
    for i in sorted(hands['twopair'], key=itemgetter(0,1,2,3,4), reverse=True):
        score+=(ranks*i[-1])
        print(f"Draw: Twopair, Hand: {i}, Bid: {i[-1]}, Rank: {ranks}")
        ranks -= 1
    for i in sorted(hands['onepair'], key=itemgetter(0,1,2,3,4), reverse=True):
        score+=(ranks*i[-1])
        print(f"Draw: Onepair, Hand: {i}, Bid: {i[-1]}, Rank: {ranks}")
        ranks -= 1
    for i in sorted(hands['highcard'], key=itemgetter(0,1,2,3,4), reverse=True):
        score+=(ranks*i[-1])
        print(f"Draw: Highcard, Hand: {i}, Bid: {i[-1]}, Rank: {ranks}")
        ranks -= 1
    return score
    
    
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
        match len(set(handlist[0:5])):
            case 1:
                hands['fivekind'].append(handlist)
            case 2:
                decide = []
                for j in set(handlist[0:5]):
                    decide.append(handlist[0:5].count(j))
                if 4 in decide:
                    hands['fourkind'].append(handlist)
                else:
                    hands['fullhouse'].append(handlist)
            case 3:
                decide = []
                for j in set(handlist[0:5]):
                    decide.append(handlist[0:5].count(j))
                if 2 in decide:
                    hands['twopair'].append(handlist)
                else:
                    hands['threekind'].append(handlist)
            case 4:
                hands['onepair'].append(handlist)
            case 5:
                hands['highcard'].append(handlist)
    print(rank_hands())



def second():
    hands['fivekind'] = []
    hands['fourkind'] = []
    hands['fullhouse'] = []
    hands['threekind'] = []
    hands['twopair'] = []
    hands['onepair'] = []
    hands['highcard'] = []
    for i in dataset:
        hand, bid = i.split(' ')
        bid = int(bid)
        handlist = []
        for char in hand:
            match char:
                case 'T':
                    handlist.append(10)
                case 'J':
                    handlist.append(1)
                case 'Q':
                    handlist.append(12)
                case 'K':
                    handlist.append(13)
                case 'A':
                    handlist.append(14)
                case _:
                    handlist.append(int(char))
        handlisttoship = handlist.copy()
        handlisttoship.append(bid)
        chardict = {}
        for loc,character in enumerate(handlist):
            if character != 1:
                chardict[character] = handlist.count(character)
        try: 
            numerous = max(chardict, key=chardict.get)
        except:
            numerous = 14
        for loc,character in enumerate(handlist):
            if character == 1:
                handlist[loc] = numerous
        match len(set(handlist[0:5])):
            case 1:
                hands['fivekind'].append(handlisttoship)
            case 2:
                decide = []
                for j in set(handlist[0:5]):
                    decide.append(handlist[0:5].count(j))
                if 4 in decide:
                    hands['fourkind'].append(handlisttoship)
                else:
                    hands['fullhouse'].append(handlisttoship)
            case 3:
                decide = []
                for j in set(handlist[0:5]):
                    decide.append(handlist[0:5].count(j))
                if 2 in decide:
                    hands['twopair'].append(handlisttoship)
                else:
                    hands['threekind'].append(handlisttoship)
            case 4:
                hands['onepair'].append(handlisttoship)
            case 5:
                hands['highcard'].append(handlisttoship)
    print(rank_hands())

if __name__ == "__main__":
    first()
    second()