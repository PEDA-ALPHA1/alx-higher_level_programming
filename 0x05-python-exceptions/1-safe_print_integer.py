#!/usr/bin/python3
def safe_print_integer(value):

    try:
        print("{:d}".format(value))
        return (True)
    except:
        return (False)
'''
def safe_print_integer(value):
   try:
       if value == int(value):
          print("{:d}".format(value))
          return (True)
   except:
      return (False)
'''
