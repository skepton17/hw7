import math

def P(n, r):
    if n<0 or r<0 or r>n:
        raise ValueError("n과 r은 n>=r>=0이여야 합니다.")
    return math.factorial(n)//math.factorial(n-r)

def C(n, r):
    if n<0 or r<0 or r>n:
        raise ValueError("n과 r은 n>=r>=0이여야 합니다.")
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

def ln(x):
    if x<=0:
        raise ValueError("ln의 지수는 0보다 커야 합니다.")
    return math.log(x)

def e(x):
    return math.exp(x)

def calc_expr(expr, x=None):
    allow={"P":P, "C":C, "ln":ln, "e":e}
    if x is not None:
        allow["x"]=x
    try:
        return eval(expr, {"__builtins__":{}}, allow)
    except:
        print("수식 오류!")