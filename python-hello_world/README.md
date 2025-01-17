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

