# data structures in python

"""
1. Linear data structures
- Arrays
- Linked List
- Stack - LIFO, LILO
- Queue
- Matrix

2. Non-linear data structures
- Binary Tree
- Heap
- Hash Table
- Graph

3. Python Specific Data Structures
- List
- Tuple
- Dictionary
- Set

4. Built-in DS
5. User-defined DS

"""

# List
"""
1. list can have homogeneous data and heterogeneous data
2. Mutable
3. Every element in the list has a specific 
"""

List = [1, 2, "hey", 7, 9]
print(List)

List = ["you", "can", "do"]
print(List)

# Nested List
List = [["hey", "you"], ["do", "it"]]
print(len(List))

# Negative indexing
List = [1, 2, 3, "hey", "abcd", 5, 6, 7, 8]
print(List[-1])
print(List[-3])

# tuples
"""
1. Immutable
2. can have homogeneous data and heterogeneous data
3. cannot add and remove in tuple
"""

Tuple = (1, 2, 4, "hey")
print(Tuple)
print(type(Tuple))

Tuple = 1, 2, 4, "hey"
print(Tuple)
print(type(Tuple))

print(Tuple[0])

# mapping
"""
1. key value pairs {key : value}
2. can have integer key 
3. separated by comma
"""

Dict = {
    "key": "value"
}
print(Dict["key"])

# by using built-in function
Dict = dict({1: "one", 2: "two"})
print(Dict)

# Set
"""
1. values have to be unique 
2. We can check for the value is there inside a set and are unordered
3. can get input with can be same elements during the creation of set
"""

Set = {1, 2, 3}
print(Set)


 