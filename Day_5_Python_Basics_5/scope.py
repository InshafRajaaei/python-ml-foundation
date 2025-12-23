# Variable creates inside a ffunction are local. 
# They do not exist outside that function.

def secret_function():
    secret_code = 12345
    return secret_code

# secret_code - this will cause an error because 'secret code' is not defined globally

print(secret_function())
