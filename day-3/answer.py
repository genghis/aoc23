from aocd import get_data
dataset = get_data(day=3, year=2023).splitlines()
reference = []

def hydrate_numbers():
    for ycoord,line in enumerate(dataset):
        newline = ""
        for i in line:
            if i != "." and not i.isnumeric():
                newline += "."
            else:
                newline += i
        # chunks = [(x,y) for (x,y) in enumerate(newline.split('.')) if y.isnumeric()]
        counter = 0
        while counter < len(newline):
            buffer = 0
            if newline[counter] == ".":
                counter+=1
            else:
                if counter+1 < len(newline) and newline[counter+1].isnumeric():
                    buffer+=1
                    if counter+2 < len(newline) and newline[counter+2].isnumeric():
                        buffer+=1
                        if counter+3 < len(newline) and newline[counter+3].isnumeric():
                            buffer+=1
                number = newline[counter:counter+buffer+1]
                tup = (number,ycoord,counter,counter+buffer)
                reference.append(tup)
                counter += buffer+1
                buffer = 0
    
def get_surrounding(ycoord,xcoord):
    surrounding = []
    if ycoord == 0:
        ymin = ycoord
    else:
        ymin = ycoord-1
    if ycoord == len(dataset):
        ymax = ycoord
    else:    
        ymax = ycoord+1
    if xcoord == 0:
        xmin = xcoord
    else:
        xmin = xcoord-1
    if xcoord == len(dataset[0]):
        xmax = xcoord
    else:
        xmax = xcoord+1
        
    listy = [x for x in range(ymin,ymax+1)]
    listx = [x for x in range(xmin,xmax+1)]
    for ycoordinate in listy:
        for xcoordinate in listx:
            surrounding.append((ycoordinate,xcoordinate))
    return(surrounding)

def find_numbers(coordlist):
    numbers = []
    for i in coordlist:
        ycoord = i[0]
        xcoord = i[1]
        for ref in reference:
            # print(ref)
            if ycoord == ref[1] and xcoord in range(ref[2], ref[3]+1):
                numbers.append(int(ref[0]))
                reference.remove(ref)
    return(numbers)
            

def first():
    hydrate_numbers()
    parts = []
    for ycoord, i in enumerate(dataset):
        for xcoord, j in enumerate(i):
            if not j.isnumeric() and j != ".":
                coordlist = get_surrounding(ycoord, xcoord)
                # print(coordlist)
                parts.extend(find_numbers(coordlist))
    # print(parts)
    print(sum(parts))
                

def second():
    pass

if __name__ == "__main__":
    first()
    second()