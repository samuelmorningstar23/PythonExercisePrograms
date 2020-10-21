def add(a,b):
    print(f"Adding {a}+{b}")
    return a+b

def substract(a,b):
    print(f"Substracting {a}-{b}")
    return a-b

def multiply(a,b):
    print(f"Multiplying {a}*{b}")
    return a*b

def divide(a,b):
    print(f"Dividing {a}/{b}")
    return a/b

def power(a,b):
    print(f"raising to the power {a}**{b}")
    return a**b


print("Let's do some math with just functions: ")

age=add(30,5)
height=substract(190,8)
weight=multiply(42,2)
iq=divide(400,2)
power=power(30,3)

print(f"Age: {age}, Height: {height}, Weight: {weight}, iq: {iq}, power: {power}")

print("Here's a Puzzle: ")
what = add(age, substract(height, multiply(weight, divide(iq,power))))

print("That becomes: ",what, "can you do it by hand?")



x = add(24, substract(divide(34,100),1023))
print("it is ",x)
