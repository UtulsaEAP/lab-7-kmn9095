while True:
    # Read input and split it into parts
    parts = input().split()
    name = parts[0]

    # Check if name is -1 to exit the loop
    if name == '-1':
        break
    #try-block 
    try:
        # Try to convert the second element to an integer and add 1 to it
        age = int(parts[1]) + 1
        print(f'{name} {age}')
    #except block to catch the exception when converting string to integer 
    except ValueError:
        # If the conversion fails, set age to 0 and print the name and age
        age = 0
        print(f'{name} {age}')

if __name__ == '__main__':
    exceptionHandling()