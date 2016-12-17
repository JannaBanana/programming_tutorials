n = int(input("insert N: "))

array = [[0 for _ in range (n)] for _ in range (n)]
x = 0
y = 0
a = 0
count = 0

while a < n :
    if a % 2 == 0:
        a += 1
        x = -1
        y = a - 1
        for _ in range (a):
            x += 1
            count += 1
            array [y][x] = count

        y = a-1
        for _ in range (a-1):
            y -= 1
            count += 1
            array [y][x] = count
    else:
        a += 1
        x = a - 1
        y = -1
        for _ in range (a):
            y += 1
            count += 1
            array [y][x] = count

        x = a-1
        for _ in range (a-1):
            x -= 1
            count += 1
            array [y][x] = count

for i in range (n):
    for j in range (n):
        print (array [i][j]," ", end="")
    print()

