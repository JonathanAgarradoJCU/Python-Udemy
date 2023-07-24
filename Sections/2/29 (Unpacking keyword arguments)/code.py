def named(**kwargs):
    print(kwargs)

details = {"name": "Bob", "age": 25}

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)
