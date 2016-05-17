''' A function that computes the fibonacci number of any parameter ''' 
def fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)
