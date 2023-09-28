def hello_world():
    print("Hello world!")

hello_world()

def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

sum(2, 3)
sum(1, 7)
sum(100, 3)

total = sum(7, 2)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Dave", last = "Gray")