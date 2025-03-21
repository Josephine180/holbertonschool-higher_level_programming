# Python - More Data Structures: Set, Dictionary
*   [Description](#description)
*   [Quiz](#quiz)

Resources
---------

**Read or watch**:

*   [Data structures](/rltoken/K8JSw_eMWjw6EzmAL1S8bQ "Data structures")
*   [Lambda, filter, reduce and map](/rltoken/JMc02-iMawLlxGCsnEalXA "Lambda, filter, reduce and map")
*   [Learn to Program 12 Lambda Map Filter Reduce](/rltoken/NnWm29rFmdDcjcdRQX1tEw "Learn to Program 12 Lambda Map Filter Reduce")

**man or help**:

*   `python3`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/XpnbqLab-uqqsit6p5ifxA "explain to anyone"), **without the help of Google**:

### General

*   Why Python programming is awesome
*   What are sets and how to use them
*   What are the most common methods of set and how to use them
*   When to use sets versus lists
*   How to iterate into a set
*   What are dictionaries and how to use them
*   When to use dictionaries versus lists or sets
*   What is a key in a dictionary
*   How to iterate over a dictionary
*   What is a lambda function
*   What are the map, reduce and filter functions

Requirements
------------

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle (version 2.7.\*)
*   All your files must be executable
*   The length of your files will be tested using `wc`

Tasks
-----

### 0\. Squared simple

Write a function that computes the square value of all integers of a matrix.

*   Prototype: `def square_matrix_simple(matrix=[]):`
*   `matrix` is a 2 dimensional array
*   Returns a new matrix:
    *   Same size as `matrix`
    *   Each value should be the square of the value of the input
*   Initial matrix should not be modified
*   You are not allowed to import any module
*   You are allowed to use regular loops, `map`, etc.

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `0-square_matrix_simple.py`

### 1\. Search and replace

Write a function that replaces all occurrences of an element by another in a new list.

*   Prototype: `def search_replace(my_list, search, replace):`
*   `my_list` is the initial list
*   `search` is the element to replace in the list
*   `replace` is the new element
*   You are not allowed to import any module

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `1-search_replace.py`

### 2\. Unique addition

Write a function that adds all unique integers in a list (only once for each integer).

*   Prototype: `def uniq_add(my_list=[]):`
*   You are not allowed to import any module

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `2-uniq_add.py`
*   
### 3\. Present in both

Write a function that returns a set of common elements in two sets.

*   Prototype: `def common_elements(set_1, set_2):`
*   You are not allowed to import any module

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `3-common_elements.py`

### 4\. Only differents

Write a function that returns a set of all elements present in only one set.

*   Prototype: `def only_diff_elements(set_1, set_2):`
*   You are not allowed to import any module

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `4-only_diff_elements.py`

### 5\. Number of keys

Write a function that returns the number of keys in a dictionary.

*   Prototype: `def number_keys(a_dictionary):`
*   You are not allowed to import any module

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `5-number_keys.py`

### 6\. Print sorted dictionary

Write a function that prints a dictionary by ordered keys.

*   Prototype: `def print_sorted_dictionary(a_dictionary):`
*   You can assume that all keys are strings
*   Keys should be sorted by alphabetic order
*   Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
*   Dictionary values can have any type
*   You are not allowed to import any module

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `6-print_sorted_dictionary.py`

### 7\. Update dictionary

Write a function that replaces or adds key/value in a dictionary.

*   Prototype: `def update_dictionary(a_dictionary, key, value):`
*   `key` argument will be always a string
*   `value` argument will be any type
*   If a key exists in the dictionary, the value will be replaced
*   If a key doesn’t exist in the dictionary, it will be created
*   You are not allowed to import any module

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `7-update_dictionary.py`

### 8\. Simple delete by key

Write a function that deletes a key in a dictionary.

*   Prototype: `def simple_delete(a_dictionary, key=""):`
*   `key` argument will be always a string
*   If a key doesn’t exist, the dictionary won’t change
*   You are not allowed to import any module

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `8-simple_delete.py`

### 9\. Multiply by 2

Write a function that returns a new dictionary with all values multiplied by 2

*   Prototype: `def multiply_by_2(a_dictionary):`
*   You can assume that all values are only integers
*   Returns a new dictionary
*   You are not allowed to import any module

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `9-multiply_by_2.py`

### 10\. Best score

Write a function that returns a key with the biggest integer value.

*   Prototype: `def best_score(a_dictionary):`
*   You can assume that all values are only integers
*   If no score found, return `None`
*   You can assume all students have a different score
*   You are not allowed to import any module

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `10-best_score.py`

### 11\. Multiply by using map

Write a function that returns a list with all values multiplied by a number without using any loops.

*   Prototype: `def multiply_list_map(my_list=[], number=0):`
*   Returns a new list:
    *   Same length as `my_list`
    *   Each value should be multiplied by `number`
*   Initial list should not be modified
*   You are not allowed to import any module
*   You have to use `map`
*   Your file should be max 3 lines
    
**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `11-multiply_list_map.py`

### 12\. Roman to Integer

**Technical interview preparation**:

*   You are not allowed to google anything
*   Whiteboard first

Create a function `def roman_to_int(roman_string):` that converts a [Roman numeral](/rltoken/COeilkCPRPmrPvaRSXcPyg "Roman numeral") to an integer.

*   You can assume the number will be between 1 to 3999.
*   `def roman_to_int(roman_string)` must return an integer
*   If the `roman_string` is not a string or `None`, return 0

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `python-more_data_structures`
*   File: `12-roman_to_int.py`
