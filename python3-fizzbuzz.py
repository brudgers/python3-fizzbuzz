
def fizzbuzz (fizz, buzz):
    first = 1
    last = 100
    end = last + 1
    cycle = fizzbuzz_cycle(fizz, buzz)
    product = fizz * buzz
    for val in range(first, end):
        index = (val - 1) % product
        if cycle[index]:
            print (cycle[index])
        else:
            print (val)

def fizzbuzz_cycle (fizz, buzz):
    """Generate a cycle of fizzes and buzzes and fizzbuzzes and False's"""
    product = fizz * buzz
    cycle = list(range(1, 1 + product))

def fb (v):
    #This function checks for fizzbuzz
    if v % product == 0:
        return "fizzbuzz"
    else: return v
    
def f (v):
   #This function checks for fizz        
    if v % fizz == 0:
        return "fizz"
    else: return v
    
def b (v):
   #This function checks for buzz 
    if v % buzz == 0:
        return "buzz"
    else: return v

def fizzbuzz_fizz_buzz_or_False (v):
   #This function returns:
   #fizzbuzz or fizz or buzz or False
   fb_val = fb(v)
   if fb_val == v:
       f_val = f(v)
       if f_val == v:
           b_val = b(v)
           if b_val == v:
               return False
           else:
               return b_val
       else:
           return f_val
   else:
       return fb_val

def fizzbuzz_cycle (fizz, buzz):
    """Generate a cycle of fizzes and buzzes and fizzbuzzes and False's"""
    product = fizz * buzz
    cycle = list(range(1, 1 + product))    

  def fb (v):
      #This function checks for fizzbuzz
      if v % product == 0:
          return "fizzbuzz"
      else: return v
      
  def f (v):
     #This function checks for fizz        
      if v % fizz == 0:
          return "fizz"
      else: return v
      
  def b (v):
     #This function checks for buzz 
      if v % buzz == 0:
          return "buzz"
      else: return v

  def fizzbuzz_fizz_buzz_or_False (v):
     #This function returns:
     #fizzbuzz or fizz or buzz or False
     fb_val = fb(v)
     if fb_val == v:
         f_val = f(v)
         if f_val == v:
             b_val = b(v)
             if b_val == v:
                 return False
             else:
                 return b_val
         else:
             return f_val
     else:
         return fb_val

  return list(map(fizzbuzz_fizz_buzz_or_False, cycle))

def fizzbuzz (fizz, buzz):
    first = 1
    last = 100
    end = last + 1
    cycle = fizzbuzz_cycle(fizz, buzz)
    product = fizz * buzz
    for val in range(first, end):
        index = (val - 1) % product
        if cycle[index]:
            print (cycle[index])
        else:
            print (val)
