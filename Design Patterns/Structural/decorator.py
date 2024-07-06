from functools import wraps

def make_blink(function):

    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)

    # Define the inner function
    def decorator():
        ret = function()

        return "<blink>" + ret + "</blink>"
    return decorator

@make_blink

def hello_world():
    return "Hello World"

print(hello_world())
print(hello_world.__name__)
print(hello_world.__doc__)