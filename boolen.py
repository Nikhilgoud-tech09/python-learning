#Booleans represent one of two values: True or False.
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  #You can create functions that returns a Boolean Value:

  def myFunction() :
  return True

print(myFunction())

#rint "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  #Python also has many built-in functions that return a boolean value, like the isinstance()

  x = 200
print(isinstance(x, int))