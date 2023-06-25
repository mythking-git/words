from collections import Counter, defaultdict
import math
import numpy as np


"""
def divideList(lst):
    group_by_len = defaultdict(list)
    for ele in lst:
        group_by_len[len(ele)].append(ele)
         
    res = []
    for key in sorted(group_by_len):
        res.append(group_by_len[key])
         
    return res
"""


r = input("length required ")
q = input("at least: ")

#f = open("allscrablewords.txt","r")
f = open("words_alpha.txt", "r")

name = f"best {r} letter words.txt"
#name = f"scrabble {r} letter words.txt"

st = []
ranked=[]
control=[]

for readline in f: 
    line_strip = readline.strip()
    control.append(line_strip)
    temp = ''.join(sorted(line_strip))
    st.append(temp)


pairedcontrol = []

for letters in range(len(control)):
    pairedcontrol.append(''.join(sorted(control[letters])))

#f = open("orderedscrable.txt", "w")
#f.write(str(st))

#control = sorted(control, key=len, reverse=True)

#dividedList = divideList(list(control))

#f = open("sortedwords.txt", "w")
#for lines in range(len(dividedList)):
#    f.write(str(lines+2) + "  -  " + str(dividedList[lines])+"\n\n\n")

#f.write(str(control))

#print(str(st))

#totals = Counter(i for i in list(itertools.chain.from_iterable(st[1])))
#print(totals)

#for count in counts: 
#    print(count)

#for val in counts:
#    print(val)

#print(list(counts)[0])

#f = open("rankedscrable.txt", "w")
#f.write(str(counts))

winners = st
counts = Counter(winners)


for key, value in counts.items():
    ranked.append([value,key])

sorted(ranked,key=lambda l:l[0], reverse=True)
#print(ranked)

sorted = sorted(ranked,key=lambda l:l[0] , reverse=True)

words=[]
bestcombo = []

finalwords = {}

f = open(name, "w")
"""
for sorts in range(len(sorted)):
    if len(sorted[sorts][1]) == int(r):
        bestcombo.append(sorted[sorts][0])"""

fact = int(math.factorial(int(r)))

#max = int(max(bestcombo))
max = 1

f.write(f"{max} out of {fact} possible letter combinations - {np.format_float_positional(((max / fact)*100), trim='-')}%\n\n" )

for x in range(len(sorted)):
    if int(r) == len(sorted[x][1]) and sorted[x][0] >= int(q):
        
        for items in range(len(control)):
            if pairedcontrol[items] == sorted[x][1]:
                finalwords.setdefault(sorted[x][1], []).append(control[items])
                #print(finalwords)

        tempstring = str(sorted[x][0]) + " - " + str(sorted[x][1]) + " - " + str(finalwords[sorted[x][1]]) + "\n"
        f.write(tempstring)

#f = open("rankedscrable.txt", "w")
#f.write(str(sorted(ranked,key=lambda l:l[0], reverse=True)))
