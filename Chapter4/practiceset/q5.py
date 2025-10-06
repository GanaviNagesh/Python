a=(7,0,8,0,0,9)
count=0
for i in range(len(a)):
    if(a[i]==0):
        count+=1
print(count)
print(a.count(0))