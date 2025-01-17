# Python - Hello, World
*   [Description](#description)
*   [Quiz](#quiz)

_For this project, we expect you to look at this concept :

*   [Python programming](/concepts/896)

Author’s disclaimer
-------------------

    Welcome to the Python world!
    
    You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
    Python has a linter / style guide, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.
    
    Enjoy!
    
    - Guillaume
    

Resources
---------

**Read or watch**:

Use this playlist as long as you are learning Python:

*   [Learn to Program](/rltoken/n9ts_nUw1YtCR9BZtGrHdQ "Learn to Program")
    
*   [Whetting Your Appetite](/rltoken/9w2S6R8vtwlmQcPg33445w "Whetting Your Appetite")
    
*   [Using the Python Interpreter](/rltoken/O87tA-o6pQ8HXAl93xxGGA "Using the Python Interpreter")
    
*   [An Informal Introduction to Python](/rltoken/x1m4AhQ1Vy9eUBaXFLRHPQ "An Informal Introduction to Python") (_Read up until “3.1.2. Strings” included_)
    
*   [How To Use String Formatters in Python 3](/rltoken/dd7bIKsC3_0wb3Np_8URUA "How To Use String Formatters in Python 3")
    
*   [Pycodestyle – Style Guide for Python Code](/rltoken/qHCPZY23PoEBaDVce2P0nw "Pycodestyle -- Style Guide for Python Code")
    

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/e_ValpdMEXoyMauk0b_SSQ "explain to anyone"), **without the help of Google**:

### General

*   How to use the Python interpreter
*   How to print text and variables using `print`
*   How to use strings
*   What are indexing and slicing in Python
*   What is the official Python coding style and how to check your code with `pycodestyle`

Requirements
------------

### Python Scripts

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.\*)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file at the root of the repo, containing a description of the repository
*   A `README.md` file, at the root of the folder of _this_ project, is mandatory
*   Your code should use the pycodestyle (version 2.7.\*)
*   All your files must be executable
*   The length of your files will be tested using `wc`

More Info
---------

### Pycodestyle

`Pycodestyle` is now the [new standard of Python style code](/rltoken/-kju7-n2p8pzvgvgbmAyPw "new standard of Python style code")

Tasks
-----

### 0\. Hello, print

mandatory

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

*   Use the function `print`

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-hello_world`
*   File: `2-print.py`

### 1\. Print integer

mandatory

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/3-print_number.py "source code") in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

*   You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/3-print_number.py "here")
*   The output of the script should be:
    *   the number, followed by `Battery street`,
    *   followed by a new line
*   You are not allowed to cast the variable `number` into a string
*   Your code must be 3 lines long
*   You have to use f-strings [tips](/rltoken/dd7bIKsC3_0wb3Np_8URUA "tips")


**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-hello_world`
*   File: `3-print_number.py`


### 2\. Print float

mandatory

Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.

*   You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/4-print_float.py "here")
*   The output of the program should be:
    *   `Float:`, followed by the float with only 2 digits
    *   followed by a new line
*   You are not allowed to cast `number` to string
*   You have to use f-strings    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-hello_world`
*   File: `4-print_float.py`


### 3\. Print string

mandatory

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/5-print_string.py "source code") in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

*   You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/5-print_string.py "here")
*   The output of the program should be:
    *   3 times the value of `str`
    *   followed by a new line
    *   followed by the 9 first characters of `str`
    *   followed by a new line
*   You are not allowed to use any loops or conditional statement
*   Your program should be maximum 5 lines long    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-hello_world`
*   File: `5-print_string.py`

### 4\. Play with strings

mandatory

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/6-concat.py "source code") to print `Welcome to Holberton School!`

*   You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/6-concat.py "here")
*   You are not allowed to use any loops or conditional statements.
*   You have to use the variables `str1` and `str2` in your new line of code
*   Your program should be exactly 5 lines long
    
**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-hello_world`
*   File: `6-concat.py`


### 5\. Copy - Cut - Paste

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/7-edges.py "source code")

*   You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/7-edges.py "here")
*   You are not allowed to use any loops or conditional statements
*   Your program should be exactly 8 lines long
*   `word_first_3` should contain the first 3 letters of the variable `word`
*   `word_last_2` should contain the last 2 letters of the variable `word`
*   `middle_word` should contain the value of the variable `word` without the first and last letters
 

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-hello_world`
*   File: `7-edges.py`

### 6\. Create a new sentence

mandatory

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/8-concat_edges.py "source code") to print `object-oriented programming with Python`, followed by a new line.

*   You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/8-concat_edges.py "here")
*   You are not allowed to use any loops or conditional statements
*   Your program should be exactly 5 lines long
*   You are not allowed to create new variables
*   You are not allowed to use string literals

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-hello_world`
*   File: `8-concat_edges.py`

### 7\. Easter Egg

mandatory

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

*   Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-hello_world`
*   File: `9-easter_egg.py`


