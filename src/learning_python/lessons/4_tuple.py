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

#or convert it into a list and convert it back into a tuple

t = (1,2,3,4,2,2,2,24,45,5,6,7,2)
print(f'orignal tuple t = {t}') 
temp = list(t)
temp.remove(2) # remove by value (or use del temp[1] for by index)
t = tuple(temp) #Output (1,3,4,...,2)
print(f'Modified tuple with convert to list, delete, convert back to t = {t}')
print(f'Print all the indexes of the number 2 in the tuple t')
indexes = [i for i, x in enumerate(t) if x == 2]
print(indexes)