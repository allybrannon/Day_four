# list of only lists
alive_inside_exogorth = [
    ['mynock 1', 'mynock 2', 'mynock 3'],
    ["parisite exogorth", "parisite exogorth"],
    ['Han', "Leia", "Chewbacca"]
]

# loop through a list of list
level_1 = 0
level_2 = 0
while(level_1 < len(alive_inside_exogorth)):
    print(alive_inside_exogorth[level_1])

    while(level_2 < len(alive_inside_exogorth[level_1])):
        print(alive_inside_exogorth[level_1][level_2])
        level_2 += 1

    level_2 = 0  # reset level_2 back to 0
    level_1 += 1

# using the for in syntax makes it much eaiser
for group in alive_inside_exogorth:
    print(group)
    for item in group:
        print(item)
