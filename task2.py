file = open("output.txt", "w")
n = input("Enter text to write to a file: ")
writing_file = file.write(n)
print(writing_file)
file.close()

file = open('output.txt', 'r')
reading_file = file.read()
print(reading_file)
file.close()

# Display confirmation message
print("Data successfully written to output.txt.")

#Enter additional data to append
file = open('output.txt', 'a')
m = input("Enter additional text to append: ")
appending_file = file.write(m)
print(appending_file)
file.close()

# Display confirmation message
print("Data successfully appended.")
