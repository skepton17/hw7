def add(*num):
    return sum(num)

def minus(first, *rest):
    result=first
    for v in rest:
        result-=v
    return result

def multiple(*num):
    res=1
    for v in num:
        res*=v
    return res

def divide(first, *num):
    result=first
    for v in num:
        if v==0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다")
        result/=v
    return result

def mean(*num):
    if len(num)==0:
        raise ValueError("숫자를 입력해야 합니다.")
    return sum(num)/len(num)
