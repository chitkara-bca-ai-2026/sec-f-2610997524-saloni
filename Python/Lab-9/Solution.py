num= int(input("Enter The Number Of Rows: "))
print("Pattern 1: Star Triangle")
print("------------------------------------------------------------")
for i in range(1,num+1):
    for j in range(i):
        print("*",end=" ")
    print( )
print(" ")
print("Pattern 2: Number Triangle")
print("------------------------------------------------------------")
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print( )
print(" ")
print("Pattern 3: Inverted Star Triangle")
print("------------------------------------------------------------")
for  i in range(num,0,-1):
    for j in range(i):
        print("*", end = " ")
    print( )
print(" ")
print("Pattern 4: Pyramid")
print("------------------------------------------------------------")
for i in range(1,num):
    for j in range(num-i):
        print(" ", end = " ")
    for k in range(2*i-1):
        print("*", end = " ")
    print( )
