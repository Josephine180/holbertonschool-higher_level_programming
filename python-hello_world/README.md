# Python - Hello, World

## Learning Objectives
At the end of this project, you should be able to:
- Use the Python interpreter.
- Print text and variables using the `print` function.
- Work with strings and perform string manipulation.
- Understand indexing and slicing in Python.
- Follow Python's official coding style using `pycodestyle`.


## Project Requirements
- Python 3.8+ is used for all scripts.
- All code is written to conform to `pycodestyle` (version 2.7.*).
- All scripts are executable and begin with `#!/usr/bin/python3`.
- Each script ends with a new line.

---

## Task

### 0. Hello, print
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print.

### Expectation : 
```Python
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
``` 

### Result 
```Python
"Programming is like building a multilingual puzzle
```

### 1. Print interger
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

- You can find the source code here
- The output of the script should be:the number, followed by Battery street,
  followed by a new line;
- You are not allowed to cast the variable number into a string;
- Your code must be 3 lines long;
- You have to use f-strings tips.

### Expectation 
```Python
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```
### Result
```Python
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")
```

### 2. Print float
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

```Python
#!/usr/bin/python3
number = 3.14159
```

# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
Objectives
The output of the program should be:
Float: followed by the float with only 2 digits
Followed by a new line.
You are not allowed to cast number to string.
You have to use f-strings.

### Expectation
```Python
#!/usr/bin/python3
number = 3.14159
print(f"Float : {number:.2f}")
```

Result
```Bash
Float : 3.14
```

### 3. Print string
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

Source code
#!/usr/bin/python3
str = "Holberton School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
Objectives
The output of the program should be:
3 times the value of str.
Followed by a new line.
Followed by the 9 first characters of str.
Followed by a new line.
You are not allowed to use any loops or conditional statement.
Your program should be maximum 5 lines long.
Expectation
#!/usr/bin/python3
str = "Holberton School"
print(f"{str * 3}")
print(str[:9])
Result
Holberton SchoolHolberton SchoolHolberton School
Holberton
4. Play with strings
Complete this source code to print Welcome to Holberton School!

Source code
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"Welcome to {str1}!")
Objectives
You are not allowed to use any loops or conditional statements.
You have to use the variables str1 and str2 in your new line of code.
Your program should be exactly 5 lines long.

### Expectation
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print(f"Welcome to {str1}!")
Result
Welcome to Holberton School!

### 5. Copy - Cut - Paste
Complete this source code.

```Python
Source code
#!/usr/bin/python3
word = "Holberton"
```

# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
Objectives
You are not allowed to use any loops or conditional statements.
Your program should be exactly 8 lines long.
word_first_3 should contain the first 3 letters of the variable word.
word_last_2 should contain the last 2 letters of the variable word.
middle_word should contain the value of the variable word without the first and last letters.

###Expectation
````Python 
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
Result
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```

### 6. Create a new sentence
Complete this source code to print object-oriented programming with Python, followed by a new line.

Source code
```Python
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
```

# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(str)
Objectives
You are not allowed to use any loops or conditional statements.
Your program should be exactly 5 lines long.
You are not allowed to create new variables.
You are not allowed to use string literals.
Expectation
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
language that combines remarkable power with very clear syntax"
str = str[39:54] + str[54:66] + str[105:111] + str[0:6]
print(str)
Result
object-oriented programming with Python

### 7. Easter Egg
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Objective
Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py).
