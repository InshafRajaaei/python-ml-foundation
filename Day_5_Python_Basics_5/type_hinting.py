# in professional environments (and in languages like c++/java), we define types.
# Python 3.5+ supports Type Hinting to indicate what data dype the function expects.
# Python ignores them at runtime, if we break them it will still run(might run sometime can fail), but the IDE will give a warning.

def greet(name: str, times: int) -> str:
    return("Hello" + name + "!  ") * times

print(greet("Alice", 5)) #valid
# print(greet(10, "Bob")) #invalid but runs