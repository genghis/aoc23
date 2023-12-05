from aocd import get_data
from pprint import pprint

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


datakeys = [y for y in [x.split(':')[0] for x in dataset]]
datavalues = [y.strip().split('\n') for y in [x.split(':')[1] for x in dataset]]
data = {k:v for (k,v) in zip(datakeys,datavalues)}

mapping = {
    'seed': {},
    'soil': {},
    'fertilizer': {},
    'water': {},
    'light': {},
    'temperature': {},
    'humidity': {},
    'location': {}}

def set_destinations(destination):
    pass

def set_source(source):
    pass

def break_maps(mapname):
    usable = mapname.split(' ')[0]
    destination = usable.split('-to-')[0]
    source = usable.split('-to-')[1]
    return (destination,source)
    

def set_mapping():
    for mapname in data.keys():
        if mapname != "seeds":
            print(mapname)
            tup = break_maps(mapname)
            destination = tup[0]
            source = tup[1]
            for datum in data[mapname]:
                # pprint(mapname)
                # pprint(datum)
                item = datum.split(' ')
                deststart = int(item[0])
                sourcestart = int(item[1])
                rng = int(item[2])
                dlist = [x for x in range(deststart, deststart+rng)]
                slist = [x for x in range(sourcestart, sourcestart+rng)]
                final = {k:v for (k,v) in zip(slist,dlist)}
                mapping[destination].update(final)
        # else:
        #     for i in data['seeds'][0].split(' '):
        #         mapping['seed'][int(i)] = 0
        

def first():
    set_mapping()
    # pprint(mapping)
    locations = []
    for seed in data['seeds'][0].split(' '):
        # print(f"Seed is {seed}")
        if int(seed) in mapping['seed'].keys():
            soil = mapping['seed'][int(seed)]
        else:
            soil = int(seed)
        # print(f"Soil is {soil}")
        if soil in mapping['soil'].keys():
            fertilizer = mapping['soil'][soil]
        else:
            fertilizer = soil
        # print(f"Fertilizer is {fertilizer}")
        if fertilizer in mapping['fertilizer'].keys():
            water = mapping['fertilizer'][fertilizer]
        else:
            water = fertilizer
        # print(f"Water is {water}")
        if water in mapping['water'].keys():
            light = mapping['water'][water]
        else:
            light = water
        # print(f"Light is {light}")
        if light in mapping['light'].keys():
            temperature = mapping['light'][light]
        else:
            temperature = light
        # print(f"Temperature is {temperature}")
        if temperature in mapping['temperature'].keys():
            humidity = mapping['temperature'][temperature]
        else:
            humidity = temperature
        # print(f"Humidity is {humidity}")
        if humidity in mapping['humidity'].keys():
            location = mapping['humidity'][humidity]
        else:
            location = humidity
        # print(f"Location is {location}")
        locations.append(location)
    # print(locations)
    print(min(locations))

def second():
    pass

if __name__ == "__main__":
    first()
    second()