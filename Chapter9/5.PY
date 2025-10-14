#sOMETIMES WE might forget to close the file after opening it but it"s necessary to close it so we can use built  keyword which we automatically close the file

with open("/workspaces/Python/Chapter9/file.txt") as f:
    print(f.read())
# When the work is completed and u leave the with loop it automatically close the file
with open("/workspaces/Python/Chapter9/myFile.txt","w") as f:
    print(f.write("Hey There How are you"))