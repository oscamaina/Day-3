def find_missing(a,b):
  """Function that returns a missing number"""
  
  a = set(a) #connverts array to list
  b = set(b)
  
  if len(a) == len(b):
    return 0
  else:
      num = set(a) ^ set(b) #symmetric difference
      num = list(num)
      return num[0]
