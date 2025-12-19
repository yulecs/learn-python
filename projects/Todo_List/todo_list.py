# Initiates the list
todo_list = []

# Reads the list file and imports the data from it into the list
with open('Todo_List.txt', 'r') as import_list:
    data_from_file = import_list.read()
    todo_list = data_from_file.splitlines()

# "Game" Loop
while True:
    # Takes an input from the player for the different options that they have
    options = int(input('What do you want to do?\n1: View list\n2: Add to list\n3: Save list to file\n4: Exit\n'))
    
    # If 1 is given prints the List into the terminal
    if options == 1:
        for i in range(len(todo_list)):
            print(f'{i+1}: {todo_list[i]}')
    
    # If 2 is given append new data into the list
    elif options == 2:
        new_data = input('What do you want to add to the list?\n')
        todo_list.append(new_data)
    
    # If 3 is given save the current list into a file
    elif options == 3:
        with open('Todo_List.txt', 'w') as file:
            for i in range(len(todo_list)):
                file.writelines(f'{i+1}: {todo_list[i]}\n')
    
    elif options == 4:
        break



