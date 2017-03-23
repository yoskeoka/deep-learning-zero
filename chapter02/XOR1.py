# -*- coding: utf-8 -*-
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = -0.5
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    tmp = AND(x1, x2)
    if tmp <= 0:
        return 1 #reverse
    else:
        return 0


print("AND(1, 1): " + str(AND(1, 1)))
print("OR(1, 0): " + str(OR(1, 0)))
print("NAND(1,1): " + str(NAND(1, 1)))

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    tmp = AND(s1, s2)
    return tmp

print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))
