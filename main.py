import math as m


def sigmoid(a):
    return 1/(1+m.exp(-1*a))


i = int(input("Enter a number to find the sigmoid function of it. "))
print(sigmoid(i))
