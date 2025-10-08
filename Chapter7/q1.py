for i in range(1,11):
    print(f"3 * {i} ={3*i}")

l=["Harry","Soham","Sachin","Rahul"]
for i in l:
    print(f"{i} hello!")
j=1
while(j<=10):
    print(f"5 * {j}={5*j}")
    j+=1

for i in range(1,4):
    print("*"*(i),end="")
    print()

for i in range(1,4):
    print(" "*(3-i),end="")
    print("*"*(2*i-1),end="")
    print()

for i in range(1,4):
    for j in range(0,3-i):
        print(" ",end="")
    for k in range(0,2*i-1):
        print("*",end="")
    print()

for i in range(1,4):
    for j in range(1,4):
        if(i==1 or i==3 or j==1 or j==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(10,0,-1):
    print(f"10 * {i} = {10*i}")

for i in range(1,7+1):
    if(i==1 or i ==7):
        print("*"*7,end="")
    else:
        print("*",end="")
        print(" "*(7-2),end="")
        print("*",end="") 
    print("")

    
    