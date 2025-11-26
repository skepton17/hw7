from . import add, minus, multiple, divide, mean
from . import power_calc, root, sine, cosine, tangent
from . import calc_expr

def get_numbers(prompt):
    nums= input(prompt).split()
    return[float(n) for n in nums]

def run_calculator():
    print("--미니 공학용 계산기--")
    while True:
        print("\n1. 덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈 5. 평균")
        print("6.거듭제곱 7. 제곱근 8. 삼각함수 9. 수식계산 0. 계산기 종료")
        choice= input("선택: ").strip()

        if choice=="0":
            print("계산기 종료")
            break

        elif choice in {'1', '2', '3', '4', '5'}:
            nums=get_numbers("숫자 입력(공백으로 구분합니다): ")
            if choice=='1': print("결과:", add(*nums))
            elif choice=='2': print("결과:", minus(nums[0], *nums[1:]))
            elif choice=='3': print("결과:", multiple(*nums))
            elif choice=='4': print("결과:", divide(nums[0], *nums[1:]))
            elif choice=='5': print("결과:", mean(*nums))

        elif choice=='6':
            below=float(input("밑 입력: "))
            e_num=float(input("지수 입력: "))
            power_calc(below, e_num)

        elif choice=='7':
            n=float(input("숫자 입력: "))
            root(n)

        elif choice=='8':
            func=input("sin/cos/tan: ").strip().lower()
            theta=float(input("각도 입력: "))
            if func=="sin": sine(theta)
            elif func=='cos': cosine(theta)
            elif func=='tan': tangent(theta)
            else: print("지원하지 않는 삼각함수 입니다.")

        elif choice=='9':
            x_val= input("x 값 입력(없으면 enter): ")
            x_val=float(x_val) if x_val else None
            expr=input("수식 입력: ")
            rest= calc_expr(expr, x_val)
            if rest is not None:
                print("결과: ", rest)

        else:
            print("0~9 중에 선택하세요")

if __name__=="__main__":
    run_calculator()