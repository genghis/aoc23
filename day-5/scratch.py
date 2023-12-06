from aocd import get_data
# dataset = get_data(day=5, year=2023).split('\n\n')

dataset = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
0 0 55'''.split('\n\n')

mapping = {}
mapping['counter'] = 0
mapping['seedlist'] = []
jank = []
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

# def we_have_to_go_backwards(payload):
#     if payload == 46:
#         print(f"LOCATION IS {payload}")
#         humidity = check(payload, "humidity", 'back')
#         print(f"HUMIDITY IS {humidity}")
#         temperature = check(humidity, "temperature", 'back')
#         print(f"TEMPERATURE IS {temperature}")
#         light = check(temperature, "light", 'back')
#         print(f"LIGHT IS {light}")
#         water = check(light, "water", 'back')
#         print(f"WATER IS {water}")
#         fertilizer = check(water, "fertilizer", 'back')
#         print(f"FERTILIZER IS {fertilizer}")
#         soil = check(fertilizer, "soil", 'back')
#         print(f"SOIL IS {soil}")
#         if soil in mapping['seeds']:
#             return payload
#         else:
#             return False
#     else:
#         return False
     
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
    
def sortfunction(payload):
    return payload[1]

def first():
    locations = []
    seedlist = mapping['seeds'][0].split(' ')
    for seed in seedlist:
        locations.append(process(int(seed)))
    print(min(locations))

jank = []

async def run_async(seedlist):
    with ThreadPoolExecutor(max_workers=1000) as executor: # Okay, I just get greedy here. There's only 5 teams but I call for 10 workers. I suspect moving to 5 would be identical but it's a lambda so it's not hurting us any. # Using session here so that it's not authing one billion times. I could be getting it wrong and maybe don't need this? Docs here http://docs.python-requests.org/en/master/user/advanced/
            loop = asyncio.get_event_loop() # Asyncio is the library that we're using to do asynchronous calls. See here: https://docs.python.org/3.6/library/asyncio-eventloops.html
            tasks = [
				loop.run_in_executor(
					executor,
					process, # The name of the function we're running in a loop
					(seed), # The variable we're passing as an argument to the function above
				)
				for seed in seedlist # Let the loop know what it should run.
			]
            for item in await asyncio.gather(*tasks):
                jank.append(item)
            
def second():
    mapping['count'] = 0
    locations = []
    array = mapping['seeds'][0].split(' ')
    # print(array)
    counter = 0
    seedlist = []
    print("hi")
    while counter < len(array):
        base = int(array[counter])
        rngmax = int(array[counter+1])
        for i in range(base, base+rngmax):
            seedlist.append(i)
        print(counter)
        counter += 2
    print("Hello")
    print(seedlist)
    # mapping['seedlist'] = seedlist
    # print(mapping['seedlist'])
    for i in seedlist:
        # print(i)
        location = process(i)
        locations.append(location)
    print(min(locations))
    # print(len(mapping['seedlist']))
    # print(min(results))
    # pool = multiprocessing.Pool(2)
    # pool.map(process, seedlist)

if __name__ == "__main__":
    # first()
    second()