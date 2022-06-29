def multiply(*args):
    total=1
    for arg in args:
        total=total*arg
    return total

def apply(*args, operator):
    if operator=="*":
        return multiply(*args)
    elif operator=="+":
        return sum(args)
    else:
        return "Not Valid"

print(apply(2,3,5, operator="+"))