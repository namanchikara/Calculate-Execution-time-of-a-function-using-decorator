from time import time

''' 
  Basically all we have to do is place @TimeOf decorator before any function say abc, and print that abc function, we shall get the time 
  this abc function took to execute, in the output(if you use print, else you can store it in some variable too, or write it to a file or
  anything.
'''

def TimeOf(func):         # This is our decorator function, which will take any function as it's argument and calculate the time required 
                          # to execute this function.

  def wrapper_func():     # wrapper function will return the time
    x = time()
    func()                
    y = time()
    
    return y-x

  return wrapper_func()


@TimeOf
def abc():
  for i in range(10000000):
    i += 1


print(abc)
