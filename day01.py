with open("data/input01.txt") as f:
    L = [int(x) for x in f.readlines()]
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i]+L[j]==2020:
            print("part 1:", L[i]*L[j])
for i in range(len(L)):
    for j in range(i+1,len(L)):
        for k in range(j+1,len(L)):
            if L[i]+L[j]+L[k]==2020:
                print("part 2:", L[i]*L[j]*L[k])