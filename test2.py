n = int(input("input N: "))

array = [[0 for _ in range (n)] for _ in range (n)]
x = 0
y = 0
count = n-1
a = 0

for a in range (1, n+1):
    y = a-1
    x = 0
    for _ in range (a):
        count += 1
        array [y][x] = count
        x += 1
        y -= 1

for a in range (n-1):
    x = a+1
    y = n-1
    for _ in range (n-1-a):
        count += 1
        array [y][x] = count
        x += 1
        y -= 1

for i in range (n):
    for j in range (n):
        print (array [i][j]," ", end="")
    print ()


