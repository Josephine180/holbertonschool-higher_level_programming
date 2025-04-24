  # Mutable and immutable objects in Python :

In Python everything is an object. An object is an entity composed of data (called attributes) and behaviors (called methods). Understanding the difference between immutable and mutable objects is essential. This concept helps improve the code’s readability, gives a better understanding of how functions work and avoids unexpected bugs. In this article we’ll look at what is an object through the notion of type and id.  Finally, we’ll explain what makes an object mutable or immutable, and why it matters so much in Python programming.

First, every object has a type, an identifier and a value. The type defines the characteristics of the object. We can find it with the function type() and it cannot be modified. The id of an object doesn’t change after his creation. It represents the memory address and is useful for checking if two objects are the same with the comparator “is”.

```
# Example with a list
a = [1, 2, 3]
```
```
# Verification of the type
print("Type of a:", type(a))  # <class 'list'>
```
```
# Verification of the id
print("ID of a:", id(a))  # Print memory adress of the object
```
```
Create an another variable  b the same list as a
b = a
```
```
# Verification if a and b are the same object with 'is'.
print("Are a and b the same object?", a is b)  # True
```
The objects can be divided into two categories : mutable and immutable. Mutable objects can be modified. In fact, we can change the value and the type without touching the identifier. List, dictionary and set are mutable objects.

```
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
```

The list has been modified but it keeps the same id (id(ma_liste)). It’s still the same object in memory.

Immutable objects are objects which cannot be modified. Specifically we found the type of int, float, strings, booleans and tuples. If we try to modify them, Python will raise an error. The mutability of an object is determined by its type and not its value.

```
# Example witt a tuple
my_tuple = (1, 2, 3)

# try to modification
try:
    my_tuple[0] = 4
except TypeError as e:
    print("Error:", e)  # TypeError: 'tuple' object does not support item assignment
```

The difference between immutable and mutable objects is important in Python because : 

Mutable objects can be modified. This modification remains even outside of the function. It can create unexpected bugs. 
Immutable objects are safer. They can’t be changed and they are great at keeping values stable and predictable.
Immutable objects are easier to manage in memory. They give better performance specially when the same value is used multiple times. 

When we modify an immutable object, we create a copy. 

```
name = "Alice"
name += " Smith" # Concatenation creates a new string object
print(name) # Output: "Alice Smith
```
With mutable objects, the original is modified.
```
my_list = [1, 2, 3]
my_list.append(4)
print(ma_liste)  # Output: [1, 2, 3, 4]
```
After having seen the difference between mutable and immutable objects, it’s important to understand how they behave when passed as arguments to functions.
In python, arguments are passed by object references. It means that functions receive a copy of the reference of the object, not a copy of the object. But, the behavior will be different if the object is mutable or not. 
If it is an immutable object, the function can’t change it and create a new object. If it is a mutable object, the function modify it. 
```
# Example with immutable object (int) :
def ajoute_1(x):
    x = x + 1  # create a new int
    print("In the function :", x)

a = 5
ajoute_1(a)
print("Outside :", a)  # 5 → not modified
```

```
# Exemple with a mutable object: 
def add_element(list):
    list.append(100)

a = [1, 2, 3]
add_elementt(a)
print(a)  # [1, 2, 3, 100] → List modified
```
In conclusion knowing the difference between mutable and immutable objects is useful in Python. It helps to write cleaner code, avoid weird bugs, and better understand how things work. 
