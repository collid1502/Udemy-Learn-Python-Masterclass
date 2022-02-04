"""
Creating a Fibonacci Funtion
"""

def fibonacci(n):
    """
    Return the `n` th Fibonacci Number, for positive `n` .

    Args:
        n (TYPE): DESCRIPTION.

    Returns:
        TYPE: DESCRIPTION.

    """
    if 0 <= n <= 1:
        return n 
    
    n_minus1, n_minus2 = 1, 0 
    
    result = None
    
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1 
        n_minus1 = result 
        
    return result 

# -----------------------------------------------------

# Run a test of the function 
for i in range(36):
    print(i, fibonacci(i))

help(fibonacci)