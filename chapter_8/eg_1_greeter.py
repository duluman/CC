"""
Functions allow you to break your programs into small parts, each of
which does one specific job. You can call a function as
many times as you want, and you can store your functions
in separate files. By using functions, you’ll be able to write
more efficient code that’s easier to troubleshoot and
maintain and that can be reused in many different programs.
"""


def greet_user():
    print("Hello!")


greet_user()


"""
When you want to use this function, you call it. A
function call tells Python to execute the code in the
function.
"""


def greeting(username="Cristian"):
    print(f"Hello, {username.title()}!")


greeting("Iulian")
greeting("Stefania")
greeting()
