# What Is a List?
# The list data type is an ordered sequence of elements that can be comprised of strings, numbers, or even other lists. 
# Lists are mutable and use zero-based indexing, meaning that the first element of the list is at index zero.

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
cities[0]  # Output: "New York"

developer = ['Python', 'Developer', 24]
# Lists can contain elements of different data types, including strings, numbers, and even other lists.

#Lists are mutable, meaning that we can change their elements after they have been created.
#To delete an element from a list, we can use the del statement.
del developer[2] # Output: ['Pyton', 'Developer']


# Using list constructors, we can create a list from a string. 
# It will create a list where each charachter in the string is an element in the list.

developer = 'Python Developer'
list(developer)  # Output: ['P', 'y', 't', 'h', 'o', 'n', ' ', 'D', 'e', 'v', 'e', 'l', 'o', 'p', 'e', 'r']


# Working withe nested lists
# A nested list is a list that contains other lists as its elements.

nested_list = [[1,2,3], [4,5,6], [7,8,9]]
nested_list[0] # Output: [1,2,3]

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2] # ['Python', 'Rust', 'C++']

print(developer[2][0]) # Output: 25