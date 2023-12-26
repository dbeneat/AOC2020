part1=0
part2=0
with open("data/input02.txt") as f:
    for lines in f:
        L = lines.split()
        a,b=L[0].split("-")
        a=int(a)
        b=int(b)
        word=L[2]
        letter=L[1][0]
        n=word.count(letter)
        if a<=n<=b:
            part1+=1
        if len(word)>=b and (bool(word[a-1]==letter)!=bool(word[b-1]==letter)):
            part2+=1
print("part 1:", part1)
print("part 2:", part2)
