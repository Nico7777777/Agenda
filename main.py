import re
f = open("agenda.in", "r+")

if __name__=='__main__':
    agenda = []
    x=1
    for linie in f:
        if x%2 == 1:
            agenda.append([linie])

        else:
            agenda[  len(agenda)-1  ].append(linie)
        x+=1
        for i in range(len(agenda)):
    print(agenda)