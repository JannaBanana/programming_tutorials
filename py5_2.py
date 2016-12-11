n = int(input ("N: "))

array = [[0 for _ in range (n)] for _ in range (n)]
x = 0
y = 0
a = 0
count = 1
count_end = n*n

for a in range(1, n+1):
    if a % 2 == 1:
        y = a-1
        x = 0
        for _ in range (a):
            array [y][x]= count
            x += 1
            count += 1

        x = a-1
        y -= 1
        for _ in range (a-1):
            array [y][x]= count
            y -= 1
            count +=1
    else:
        x = a -1
        y = 0
        for _ in range (a):
            array [y][x] = count
            y += 1
            count += 1

        x -= 1
        y -= 1
        for _ in range (a-1):
            array [y][x] = count
            x -= 1
            count += 1

for i in range(n+1):
    for j in range(n+1):
        print(array[i][j], ' ', end="")
    print()
