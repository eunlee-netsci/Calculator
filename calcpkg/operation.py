# def add(a, b):
#     return a + b

# def sub(a, b): 
#     return a-b

# def multi(a, b) : 
#     return a * b 

# def divide(a, b) : 
#     return a/b

def add(a, b):
    try: 
        c = a + b
        return c  
    except Exception as e : 
        print('Error raised:', e)
    

def sub(a, b): 
    try : 
        c = a - b 
        return c 
    except Exception as e : 
        print('Error raised:', e)
    

def multi(a, b) : 
    try : 
        c = a * b 
        return c 
    except Exception as e : 
        print('Error raised:', e)
    

def divide(a, b) : 
    try : 
        c = a/b
        return c
    except Exception as e : 
        print('Error raised:', e)


