#code made by JUAN FELIPE MARTINEZ 29/01/2024
#version 1.0
import math


def complex_add(a,b):
    pr = a[0] + b[0]
    pi = a[1] + b[1]
    return (pr, pi)

def complex_subs(a,b):
    pr = a[0] - b[0]
    pi = a[1] - b[1]
    return (pr, pi)

def complex_mult(a,b):
    pr = (a[0]*b[0]) - (a[1]*b[1])
    pi = (a[0]*b[1]) + (a[1]*b[0])
    return (pr, pi)

def complex_div(a,b):
    pr = ((a[0]*b[0]) + (a[1]*b[1])) / ((b[0]**2) + (b[1]**2))
    pi = ((a[1]*b[0]) - (a[0]*b[1])) / ((b[0]**2) + (b[1]**2))
    return (pr, pi)

def complex_modul(a):
    pr = math.sqrt(a[0]**2 + a[1]**2)
    print("modulo", pr)
    return pr

def complex_conj(a):
    pr = a[0]
    pi = a[1]*(-1)
    print("conjugada", pr,pi)
    return (pr, pi)

def complex_fase(a):
    pr = math.atan2(a[1],a[0])
    print("fase",pr)
    return pr

def complex_cartesianoPolar(a):
    pr = complex_modul(a)
    pi = complex_fase(a)
    print("cartesiano a polar ", pr, pi)
    return (pr, pi)

def complex_polarCartesiano(a):
    pr = a[0] * math.cos(a[1])
    pi = a[0] * math.sin(a[1])
    print("polar a cartesiano",pr, pi)
    return (pr, pi)

def main():
    a = [float(x) for x in input().strip().split(',')]
    b = [float(x) for x in input().strip().split(',')]
    print(complex_add(a,b))
    print(complex_subs(a,b))
    print(complex_mult(a,b))
    print(complex_div(a,b))
    print(complex_modul(a))
    print(complex_conj(a))
    print(complex_cartesianoPolar(a))
    print(complex_polarCartesiano(a))
    print(complex_fase(a))

if __name__ == "__main__":
    main()
