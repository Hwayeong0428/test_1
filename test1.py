# 덧셈 함수
def add(x, y):
    return x + y

# 뺄셈 함수
def subtract(x, y):
    return x - y

# 곱셈 함수
def multiply(x, y):
    return x * y

# 나눗셈 함수
def divide(x, y):
    return x / y

print("계산할 연산을 선택하세요.")
print("1. 덧셈")
print("2. 뺄셈")
print("3. 곱셈")
print("4. 나눗셈")

# 사용자로부터 선택 받기
choice = input("선택(1/2/3/4): ")

num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("잘못된 입력입니다.")
    # 추가추가
# 추가추가
