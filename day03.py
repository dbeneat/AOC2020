with open("data/input03.txt") as f:
    puzzle=[line.rstrip() for line in f.readlines()]

def f(dx,dy):
    res=0
    x=0
    for y in range(dy,len(puzzle),dy):
        x=(x+dx)%len(puzzle[0])
        if puzzle[y][x]=="#":
            res+=1
    return res
print("part 1:",f(3,1))

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
part2=1
for x in slopes:
    part2*=f(*x)
print("part 2:",part2)
