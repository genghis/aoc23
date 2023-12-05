from aocd import get_data
from concurrent.futures import ThreadPoolExecutor
import asyncio
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
        if val in range(nextstart,nextstart+rngmax):
            offset = nextstart-prevstart
            # offset = prevstart-nextstart
            return(val-offset)
    return val 

def we_have_to_go_backwards(payload):
    if payload == 46:
        print(f"LOCATION IS {payload}")
        humidity = check(payload, "humidity", 'back')
        print(f"HUMIDITY IS {humidity}")
        temperature = check(humidity, "temperature", 'back')
        print(f"TEMPERATURE IS {temperature}")
        light = check(temperature, "light", 'back')
        print(f"LIGHT IS {light}")
        water = check(light, "water", 'back')
        print(f"WATER IS {water}")
        fertilizer = check(water, "fertilizer", 'back')
        print(f"FERTILIZER IS {fertilizer}")
        soil = check(fertilizer, "soil", 'back')
        print(f"SOIL IS {soil}")
        if soil in mapping['seeds']:
            return payload
        else:
            return False
    else:
        return False

def process(seed):
    soil = check(int(seed), "soil")
    fertilizer = check(soil, "fertilizer")
    water = check(fertilizer, "water")
    light = check(water, "light")
    temperature = check(light, "temperature")
    humidity = check(temperature, "humidity")
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
    megacounter = 0
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
    mapping['seeds'] = seedlist
    # location_list = []
    # for payload in mapping['location']:
    #     values = payload.split(" ")
    #     location_list.append(values)
    # location_list.sort(key=sortfunction)
    # print(location_list)
    # answers = []
    # answer = False
    # for locale in location_list:
    #     item = int(locale[0])
    #     rngmax = int(locale[2])
    #     for n in range(item, item+rngmax):
    #         answer = we_have_to_go_backwards(n)
    #         if answer:
    #             print(n)
    #             break
    # print(mapping['seeds'])
    # print(min(answer))
    # loop = asyncio.get_event_loop()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run_async(seedlist)) # This determines what function is running in a loop. So this has loops on loops on loops. Probably there's a more efficient way to do this.
    loop.run_until_complete(future) 
    # lst = run_async(seedlist)
    print(min(jank))


    # for seed in seedlist:
    #     pool.submit()

if __name__ == "__main__":
    first()
    second()