filename = input("Enter filename: ")
try:
    with open(filename, 'r') as file:
        print(file.read())

except FileNotFoundError:
    with open(filename, 'w') as file:
        file.write("File is opened in write mode")