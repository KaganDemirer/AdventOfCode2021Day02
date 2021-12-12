with open("02_Advent.txt") as input_files:
    lines = input_files.readlines()

horizontal=0
depth=0
aim=0

def dive():
    global horizontal
    global depth
    for x in lines:
        x = x.replace("\n","")
        if "forward" in x:
            horizontal=horizontal+int(x[-1])
        elif "up" in x:
            depth=depth-int(x[-1])
        elif "down" in x:
            depth=depth+int(x[-1])
    print(horizontal, depth, horizontal*depth)

def dive_with_aim():
    global horizontal
    global depth
    global aim
    for x in lines:
        x = x.replace("\n","")
        if "forward" in x:
            horizontal=horizontal+int(x[-1])
            depth=depth+aim*int(x[-1])
        elif "up" in x:
            aim=aim-int(x[-1])
        elif "down" in x:
            aim=aim+int(x[-1])
    print(horizontal, depth, aim, horizontal*depth)

dive()