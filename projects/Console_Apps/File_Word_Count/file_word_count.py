import os

# Open the file in reading mode
with open('./projects/File_Word_Count/file.txt', "r") as file:
    # Read the contents of the file
    contents = file.read()
    
    # Print the number of characters in the file
    print(f'Character Count: {len(contents)}')
    
    # Remove special symbols and separate by spaces
    contents = contents.strip(".?,:'")
    contents = contents.split()
    
    # Print the number of words in the file
    print(f'Word Count: {len(contents)}')
    