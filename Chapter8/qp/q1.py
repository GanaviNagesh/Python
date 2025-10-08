# celcisus to farhniet
def temp(c):
    return (c*9/5)+32
print(f"{(temp(25))} °f")

# suum of n natural numbers
def sum(n):
    if(n<=0):
        return n
    return n+sum(n-1)
print(sum(5))

# a python function to remove a given word from a lst add strip it at the smae time
l=["apple","mango","cherry","Melon"]
word="mango"
for i in l:
    if(i==word):
        l.remove(i)
        break
print(l)

def rem(l,word):
    n=[]
    for item in l:
        if not(item ==word):
            n.append(item.strip(word))
    return n

l=["Harry","Rohan","Shubhan","an"]
print(rem(l,"an"))