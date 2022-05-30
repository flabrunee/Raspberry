x = "awesome"

def myfunc():
  global x
  x = "hola"
  print("Python is " + x)
  
myfunc()
print(x)