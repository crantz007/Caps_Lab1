# Write a program that asks for the names of all of the classes you are taking this semester
# Save these class names in a list

# input
classes = int(input("How many classes do you have ? "))
i = 0
# creating list
class_list = []
while i < classes:
    i = i + 1
    class_list.append(input("Enter the name of the class:\n"))

print("{:s}\n{:s}\n".format("The classes you are taking are :.", len("The classes you are taking are: ") * "-"))
for line in class_list:
    # Output

    print(line)
