# Write a program that asks for your name and the month you were born in

# input name
name = (input("What is your name ? "))

# Count Letters in name and ignoring space
numberOfLetter = len(name) - name.count(" ")

# input month
month = input("What month you were born in ? ")

# ignore Case
ignoreCase = month.lower()

# Output
print(f'Good Morning!!! {name}\n')
print(f'There are {numberOfLetter} Letters in your name\n')

# checking if birthday is in January
if ignoreCase == 'january':
    print('Happy Birthday')
else:
    print('Your birthday is not on this month (January)')
