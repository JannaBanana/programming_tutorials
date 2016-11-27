import sys

n = int(input("insert: "))
count = 0
for i in range (0, 2*n-1):
    if i < n:
            for j in range (0, n):
                if i+j<n-1:
                    print ("_"," ", end="")
                else:
                    count = count + 1
                    print(count, " ", end="")
                sys.stdout.flush()
    # else:
    #         for j in range (n, 2*n-1):
    #             if i+j>=2:
    #                 print ("_"," ", end="")
    #             else:
    #                 count = count +1
    #                 print(count, " ", end="")
    #         sys.stdout.flush()
    print ("\n")


# n = 5
# count = 0
# for i in range(0, n):
#     for j in range(3):
#         count = count + 2
#         print(count, ' ', end="")
#     print()

