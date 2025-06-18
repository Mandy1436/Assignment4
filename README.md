# Assignment4
# Module 5: Files, Exceptions, and Errors in Python

In this python program, we will try to read the content of a text file(which is already exist)
1. Start a try block

The code begins with a try: statement. This means Python will try to run the code inside this block. If there is an error (like the file not being found), it will jump to the except block.

2. Open the file

file1 = open('sample.txt', 'r')

This line tries to open a file named sample.txt in read mode ('r').

If the file exists, it is opened and assigned to the variable file1.

3. Read the file

reading_file = file1.read()

This reads the entire contents of sample.txt and stores it in the variable reading_file.

4. Print the file content

print(reading_file)

This prints whatever was read from the file to the screen.

5. Handle file not found error

If sample.txt does not exist, Python raises a FileNotFoundError.

The code jumps to the except FileNotFoundError: block.

6. Print error message

print("The File sample.txt was not found.")

This line runs only if the file was not found. It shows a clear message instead of crashing the program.

#Task 2

Open a file for writing
file = open("output.txt", "w")
This opens (or creates) the file output.txt in write mode ("w"). If the file exists, its content will be erased.
2. Get user input
n = input("Enter text to write to a file: ")
Asks the user to enter some text, which is stored in variable n.
3. Write input to the file
writing_file = file.write(n)
Writes the user's input to output.txt. The write() method returns the number of characters written, which is saved in writing_file.
4. Print the number of characters written
print(writing_file)
Displays the number of characters that were written to the file.
5. Close the file
file.close()
Closes output.txt to save changes and free system resources.
6. Open the file for reading
file = open('output.txt', 'r')
Opens output.txt in read mode ("r").
7. Read the file content
reading_file = file.read()
Reads the entire content of output.txt and stores it in reading_file.
8. Print the file content
print(reading_file)
Displays the content that was just written to the file.
9. Close the file
file.close()
Closes the file after reading.
10. Display confirmation message
print("Data successfully written to output.txt.")
Shows a message confirming that data was written.
11. Open the file for appending
file = open('output.txt', 'a')
Opens output.txt in append mode ("a"), so new data will be added at the end of the file without erasing existing content.
12. Get additional user input
m = input("Enter additional text to append: ")
Asks the user for more text to add to the file, storing it in m.
13. Append the input to the file
appending_file = file.write(m)
Appends the new text to output.txt. Again, write() returns the number of characters written.
14. Print the number of characters appended
print(appending_file)
Displays the number of characters added.
15. Close the file
file.close()
Closes the file after appending.
16. Display confirmation message
print("Data successfully appended.")
Shows a message confirming that data was appended to the file.

