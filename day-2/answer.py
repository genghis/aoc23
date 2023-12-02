from aocd import get_data
dataset = get_data(day=2, year=2023).splitlines()

def first():
    games = []
    for i in dataset:
        maxes = {"red": 0, "green": 0, "blue": 0}
        num, turns = i.split(": ")
        num = num.replace("Game ", "")
        turnlist = turns.split("; ")
        for j in turnlist:
            draws = j.split(", ")
            for k in draws:
                number, color = k.split(" ")
                if maxes[color] < int(number):
                    maxes[color] = int(number)
        if maxes["red"] <= 12 and maxes["green"] <= 13 and maxes["blue"] <= 14:
            games.append(int(num))
    print(sum(games))

def second():
    games = []
    for i in dataset:
        maxes = {"red": 0, "green": 0, "blue": 0}
        num, turns = i.split(": ")
        num = num.replace("Game ", "")
        turnlist = turns.split("; ")
        for j in turnlist:
            draws = j.split(", ")
            for k in draws:
                number, color = k.split(" ")
                if maxes[color] < int(number):
                    maxes[color] = int(number)
        games.append(maxes["green"]*maxes["blue"]*maxes["red"])
    print(sum(games))

if __name__ == "__main__":
    first()
    second()