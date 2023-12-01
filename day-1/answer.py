from aocd import get_data
dataset = get_data(day=1, year=2023)
# dataset = '''two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen'''

wordnumbers = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
        }

def first():
    numbers = []
    for i in dataset.splitlines():
        numerics = []
        for j in i:
            if j.isnumeric():
                numerics.append(j)
        result = int(f"{numerics[0]}{numerics[-1]}")
        numbers.append(result)
    print("FIRST")
    print(sum(numbers))

def second():
    numbers = []
    for i in dataset.splitlines():
        numerics = []
        for index,character in enumerate(i):
            if character.isnumeric():
                numerics.append(character)
            elif i[index:index+2] in wordnumbers.keys():
                numerics.append(wordnumbers[i[index:index+2]])
            elif i[index:index+3] in wordnumbers.keys():
                numerics.append(wordnumbers[i[index:index+3]])
            elif i[index:index+4] in wordnumbers.keys():
                numerics.append(wordnumbers[i[index:index+4]])
            elif i[index:index+5] in wordnumbers.keys():
                numerics.append(wordnumbers[i[index:index+5]])
        result = int(f"{numerics[0]}{numerics[-1]}")
        numbers.append(result)
    print("SECOND")
    print(sum(numbers))
        
if __name__ == "__main__":
    first()
    second()