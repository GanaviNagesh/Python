with open("/workspaces/Python/Chapter9/PracticeSet/poems.txt") as f:
    found=False
    for line in f:
        if "you" in line.lower():
            print(line)
            found=True
            break
    if not found:
        print("Not Found")
        