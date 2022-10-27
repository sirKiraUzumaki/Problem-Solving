#Part-1
text_file = open("./Data/day5.txt")
q = text_file.read().split("\n")

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

n = []
for i in q:
    if (i.count('a')+i.count('e')+i.count('i')+i.count('o')+i.count('u') >= 3):
        for j in a:
            if (j+j in i):
                if ('ab' not in i and 'cd' not in i and 'pq' not in i and 'xy' not in i):   
                    n.append(i)

print(len(set(n)))

#Part-2
n1 = 0
for i in range(len(q[0])):
    for j in range(0, i+1):
        if (q[0][i],q[0][i+1] == q[0][j-i-2],q[0][j-i-1]):
            n1+=1
            
print(n1)
