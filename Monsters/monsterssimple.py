textfile = 'monsters_simple.txt'

#Initalises a dictionary
monsters_dict = {}

#Opens the file indicated by the variable declared earlier and identifies the file as the variable file
with open(textfile,'r') as file:
    #Skips the first line
    next(file)
    
    for line in file:
        my_list = line.split(',')
        monsters_dict[my_list[0]] = (my_list[1])[:-1]
    
print('----------------------------------------------------------------')
print('Monsters list:')
for key in monsters_dict.keys():
    print(key)    
print('----------------------------------------------------------------\n')

    
while True:
    monster_name = input('Monster name? Must be case-sensitive\n')
    if monster_name in monsters_dict.keys():
        print('Description:',monsters_dict[monster_name])
        print()
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() == 'n':
            break
    else:
        print("Monster not found\n")
