f=open("/workspaces/Python/Chapter9/file.txt")
# lines=f.read()
# #return a list
# print(lines,type(lines))
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()