#Strings in python are surrounded by either single quotation marks, or double quotation marks.

print("hello")
print('hello')

#You can assign a multiline string to a variable by using three quotes:

a = """hi choit how a r u,
what are u doing."""
print(a)

#strings in Python are arrays of unicode characters.
a = 'Hi, Nikhil'
print(a[3])

#to get a length of a string
a = 'nikhil'
print(len(a))

#To check if a certain phrase or character is present in a string,
txt = "nikhil doing something"
print("doing" in txt) 
# also we will use if statment in 
txt = "nikhil doing something"
if "doing" in txt:
    print("yes, 'doing' is present.")

#To check if a certain phrase or character is NOT present in a string

txt = "The best things in life are free!"
print("expensive" not in txt)



