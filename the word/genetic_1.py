import random

def boo(x,y,z):
    return 6*x+y*42+z*99 - 650

def fitness(x,y,z):
    ans = boo(x,y,z)
    if ans == 0:
        return 99999
    else:
        return abs(1/ans)

solutions = []

for i in range(1000):
    solutions.append(
        (random.uniform(0,10000),random.uniform(0,10000),random.uniform(0,10000))
    )

for i in range(1000):
    rank = []
    for j in solutions:
        rank.append( (fitness(j[0],j[1],j[2]),j) )
    rank.sort()
    rank.reverse()

    print(f"=== Gen {i} best solutions === ")
    print(rank[0])

    if rank[0][0] > 9999:
        break
    
    best = rank[:100]
    
    ele = []
    for t in best:
        ele.append(t[1][0])
        ele.append(t[1][1])
        ele.append(t[1][2])

    new = []
    for _ in range(1000):
        e1 = random.choice(ele) * random.uniform(0.99,1.01)
        e2 = random.choice(ele) * random.uniform(0.99,1.01)
        e3 = random.choice(ele) * random.uniform(0.99,1.01)
        new.append((e1,e2,e3))

    solutions = new