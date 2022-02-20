import random
n = int(input())
while n == len(list):
    g = random.randint(0 , 30)
    if g not in  list:
        list.append(g)
print(list)