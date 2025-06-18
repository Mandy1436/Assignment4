'''# How to open and read a file in Python with error handling

file1 = open('sample.txt', 'r')
reading_file = file1.read()
print(reading_file)
file1.close()
'''


# task_with_try_except_finally.py

try:
    # Attempt to open the file
    file1 = open('sample.txt', 'r')

    # Attempt to read the file
    reading_file = file1.read()

    # Attempt to print the content
    print(reading_file)

except FileNotFoundError:
    # This block executes if sample.txt does not exist
    print("The File sample.txt was not found.")
