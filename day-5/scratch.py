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
# 56 93 4
# 0 0 55'''.split('\n\n')

mapping = {}
mapping['counter'] = 0
mapping['seedlist'] = []

mapping2 = {}
jank = []
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

def check(val,key, *argv):
    for i in mapping[key]:
        nums = i.split(' ')
        rngmax = int(nums[2])
        if 'back' in argv:
            nextstart = int(nums[0])
            prevstart = int(nums[1])
        else:
            prevstart = int(nums[0])
            nextstart = int(nums[1])
        if nextstart <= val <= nextstart+rngmax:
            offset = nextstart-prevstart
            # offset = prevstart-nextstart
            return(val-offset)
    return val 

def check2(val,key, *argv):
    minimum, maximum = val[0], val[1]
    for i in mapping2[key]:
        prev = i[1]
        next = i[0]
        offset = prev[0]-next[0]
        if prev[0] <= minimum < maximum <= prev[1]:
            newmin = minimum-offset
            newmax = maximum-offset
            return((newmin-1,newmax-1))
        elif minimum <= prev[0] < prev[1] <= maximum:
            newmin = minimum-offset
            newmax = next[1]
            goodrange = (newmin-1,newmax-1)
            badrange = (prev[1], maximum)
            process2(badrange, key)
            return(goodrange)
        elif minimum <= prev[0] < maximum <= prev[1]:
            newmin = next[0]
            newmax = maximum
            goodrange = (newmin-1,newmax-1)
            badrange = (minimum,prev[0])
            process2(badrange, key)
            return(goodrange)
        elif minimum < maximum <= prev[0] or prev[1] <= minimum < maximum:
            return val
    return val

def process(seed):
    soil = check(int(seed), "soil")
    print(f"SOIL IS {soil}")
    fertilizer = check(soil, "fertilizer")
    print(f"FERTILIZER IS {fertilizer}")
    water = check(fertilizer, "water")
    print(f"WATER IS {water}")
    light = check(water, "light")
    print(f"LIGHT IS {light}")
    temperature = check(light, "temperature")
    print(f"TEMPERATURE IS {temperature}")
    humidity = check(temperature, "humidity")
    print(f"HUMIDITY IS {humidity}")
    location = check(humidity, "location")
    return(location)

def process2(seed, startingpt):
    if startingpt == "soil":
        print(f"SEED IS {seed}")
        soil = check2(seed, "soil")
        print(f"SOIL IS {soil}")
        fertilizer = check2(soil, "fertilizer")
        print(f"FERTILIZER IS {fertilizer}")
        water = check2(fertilizer, "water")
        print(f"WATER IS {water}")
        light = check2(water, "light")
        print(f"LIGHT IS {light}")
        temperature = check2(light, "temperature")
        print(f"TEMPERATURE IS {temperature}")
        humidity = check2(temperature, "humidity")
        print(f"HUMIDITY IS {humidity}")
        location = check2(humidity, "location")
        print(f"LOCATION IS {location}")
    elif startingpt == "fertilizer":
        fertilizer = check2(seed, "fertilizer")
        print(f"FERTILIZER IS {fertilizer}")
        water = check2(fertilizer, "water")
        print(f"WATER IS {water}")
        light = check2(water, "light")
        print(f"LIGHT IS {light}")
        temperature = check2(light, "temperature")
        print(f"TEMPERATURE IS {temperature}")
        humidity = check2(temperature, "humidity")
        print(f"HUMIDITY IS {humidity}")
        location = check2(humidity, "location")
        print(f"LOCATION IS {location}")
    elif startingpt == "water":
        water = check2(seed, "water")
        print(f"WATER IS {water}")
        light = check2(water, "light")
        print(f"LIGHT IS {light}")
        temperature = check2(light, "temperature")
        print(f"TEMPERATURE IS {temperature}")
        humidity = check2(temperature, "humidity")
        print(f"HUMIDITY IS {humidity}")
        location = check2(humidity, "location")
        print(f"LOCATION IS {location}")
    elif startingpt == "light":
        light = check2(seed, "light")
        print(f"LIGHT IS {light}")
        temperature = check2(light, "temperature")
        print(f"TEMPERATURE IS {temperature}")
        humidity = check2(temperature, "humidity")
        print(f"HUMIDITY IS {humidity}")
        location = check2(humidity, "location")
        print(f"LOCATION IS {location}")
    elif startingpt == "temperature":
        temperature = check2(seed, "temperature")
        print(f"TEMPERATURE IS {temperature}")
        humidity = check2(temperature, "humidity")
        print(f"HUMIDITY IS {humidity}")
        location = check2(humidity, "location")
        print(f"LOCATION IS {location}")
    elif startingpt == "humidity":
        humidity = check2(seed, "humidity")
        print(f"HUMIDITY IS {humidity}")
        location = check2(humidity, "location")
        print(f"LOCATION IS {location}")
    elif startingpt == "location":
        location = check2(seed, "location")
        print(f"LOCATION IS {location}")
    jank.append(location[0])
    return(location)

def sortfunction(payload):
    return payload[1]

def create_ranges():
    for key in mapping.keys():
        if key != "counter" and key != "count" and key != "seeds":
            for i in mapping[key]:  
                nums = i.split(' ')
                rngmax = int(nums[2])
                nextstart = int(nums[0])
                prevstart = int(nums[1])
                nexttup = (nextstart, nextstart+rngmax)
                prevtup = (prevstart, prevstart+rngmax)
                if mapping2.get(key):
                    mapping2[key].append((nexttup,prevtup))
                else:
                    mapping2[key] = [(nexttup,prevtup)]

def seeds_ranges():
    seedlist = []
    for i in mapping['seeds'][0].split(' '):
        seedlist.append(i)
    for i in range(0, len(seedlist), 2):
        seedtup = (int(seedlist[i]), int(seedlist[i])+int(seedlist[i+1]))
        if mapping2.get('seeds'):
            mapping2['seeds'].append(seedtup)
        else:
            mapping2['seeds'] = [seedtup]

def first():
    locations = []
    seedlist = mapping['seeds'][0].split(' ')
    for seed in seedlist:
        locations.append(process(int(seed)))
    print(min(locations))

def second():
    mapping['counter'] = 0
    locations = []
    create_ranges()
    seeds_ranges()
    # print(mapping2)
    for i in mapping2['seeds']:
        process2(i,"soil")
    print(jank)
    print(min(jank))
    

if __name__ == "__main__":
    # first()
    second()