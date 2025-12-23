# docstrings describe what a function does.
# Syntax: triple qoutes """ inside the function.
# Access: can read the using help(function_name) or function_name.__doc__

def power(base, exponent):
    """
    Calculates the power of a number.
    
    Args:
        base (int): The base number.
        exponent (int): The power to raise to.
        
    Returns:
        int: The result of base ** exponent.
    """
    return base ** exponent

print(power(2, 3))  # 8
print(power.__doc__)
#print(help(power))