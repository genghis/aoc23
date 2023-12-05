from aocd import get_data
dataset = get_data(day=5, year=2023).split('\n\n')

# dataset = '''seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4'''.split('\n\n')

mapping = {}

for i in dataset:
    chunks = i.split(':')
    if chunks[0] != "seeds":
        name = chunks[0].split('-to-')[1].replace(" map", "")
    else:
        name = "seeds"
    if len('chunks1') > 1:
        entries = chunks[1].strip().split('\n')
    else:
        entries = chunks[1].strip()
    mapping[name] = entries
    
def check(val,key):
    for i in mapping[key]:
        nums = i.split(' ')
        prevstart = int(nums[0])
        nextstart = int(nums[1])
        rngmax = int(nums[2])
        # print(f"Val = {val}\nRange = {prevstart}-")
        if val in range(nextstart,nextstart+rngmax):
            # print(f"{prevstart} through {prevstart+rngmax}")
            offset = nextstart-prevstart
            # print(f"Offset is {offset}")
            return(val-offset)
    return val 

# def process_backwards(val, key):
#     for i in mapping 
#     humidity = check(temperature, "humidity")
#     temperature = check(light, "temperature")
#     light = check(water, "light")
#     water = check(fertilizer, "water")
#     fertilizer = check(soil, "fertilizer")
#     soil = check(int(seed), "soil")
    
def process(seed):
    print(f"Seed = {seed}")
    soil = check(int(seed), "soil")
    print(f"Soil = {soil}")
    fertilizer = check(soil, "fertilizer")
    print(f"Fertilizer = {fertilizer}")
    water = check(fertilizer, "water")
    print(f"Water = {water}")
    light = check(water, "light")
    print(f"Light = {light}")
    temperature = check(light, "temperature")
    print(f"Temperature = {temperature}")
    humidity = check(temperature, "humidity")
    print(f"Humidity = {humidity}")
    location = check(humidity, "location")
    print(f"Location = {location}")
    return(location)
    
def first():
    locations = []
    seedlist = mapping['seeds'][0].split(' ')
    for seed in seedlist:
        locations.append(process(int(seed)))
    print(min(locations))
        

def second():
    locations = []
    array = mapping['seeds'][0].split(' ')
    counter = 0
    seedlist = []
    while counter < len(array):
        base = int(array[counter])
        rngmax = int(array[counter+1])
        for i in range(base, base+rngmax):
            seedlist.append(i)
        counter += 2
    for seed in seedlist:
        locations.append(process(int(seed)))
    print(min(locations))

if __name__ == "__main__":
    first()
    second()