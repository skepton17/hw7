import math

def power_calc(base, pow):
    print(base**pow)

def root(num):
    if num<0:
        raise ValueError("음수는 제곱근에 넣을 수 없습니다.")
    else:
        print(num**0.5)

def sine(theta):
    rad=math.radians(theta)
    result=math.sin(rad)
    print("sin({})={}".format(theta, result))
    return result

def cosine(theta):
    rad=math.radians(theta)
    result=math.cos(rad)
    print("cos({})={}".format(theta, result))
    return result

def tangent(theta):
   rad=math.radians(theta)
   result=math.tan(rad)
   print("tan({})={}".format(theta, result))