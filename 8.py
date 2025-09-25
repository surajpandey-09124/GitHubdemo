# Write, append, and read a file

# Take user input and write to file
user_input = input("Enter some text: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Append additional data
with open("output.txt", "a") as file:
    file.write("This is additional data.\n")

# Read and display final content
with open("output.txt", "r") as file:
    content = file.read()
    print("Final content of the file:")
    print(content)
