# We know locan varibale can not be seen outside of a function. 
# If we want to use a variable globally, we can declare that variable as global using the 'global' keyword.

score = 0
def update_score(points):
    global score
    score += points

update_score(55)
print(score)  #55

# Warning: Using global variables can make code harder to understand and debug.