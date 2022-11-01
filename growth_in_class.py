
classr = []
for i in range(11):
    classr.append({"stat":0, "cnt":0})

with open("sometext.txt") as inf:
    for line in inf:
        line = line.split("\t")
        classr[int(line[0]) - 1]["stat"] += int(line[2])
        classr[int(line[0]) - 1]["cnt"] += 1

for i in range(11):
    print(str(i + 1) + " ", end='')
    if classr[i]["stat"] != 0:
        print(classr[i]["stat"]/ classr[i]["cnt"])
    else:
        print("-")    