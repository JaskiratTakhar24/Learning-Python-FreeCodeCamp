# A tuple is a python data type just like a list, but it is immutable. 
#It means that once a tuple is created, we cannot change its elements.

#List vs tuple
developer = ['Python', 'Developer', 24] # this is a list which is enclosed in square brackets
developer_tuple = ('Python', 'Developer', 24) # this is a tuple which is enclosed in parenthesis

# to add an element to a tuple, we can use the + operator to concatenate two tuples togeather.

developer_tuple = developer_tuple + ('Jaskirat',) # we need to add a comma after the element to indicate that it is a tuple with one element
print(developer_tuple) # Output: ('Python', 'Developer', 24, 'Jaskirat')

#Deleting from tuple doesn't work since they are immutable
#However the you can use slicing in such a way that it performs the operation and re-assign the tuple back to orignal variable

deserts = ('cake', 'pie', 'cookie', 'ice cream')
deserts = deserts[1:] # Output: ('pie', 'cookie', 'ice cream')
