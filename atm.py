# balance : 초기 잔액을 설정하는 변수를 초기화해주세요
# 금액은 여러분 마음대로 설정해주세요

# 사용자로부터 atm 기계에 사용 목적에 맞는 기능을 선택할 수 있도록
# 기능 입력을 받는 기능을 구현해주세요


balance = 100000000


while True:
    num = input("사용하실 기능을 선택해주세요 (1. 입금, 2. 출금, 3. 명세표 출력, 4. 종료) : ")

    if num == '4':  # 종료
        break

    if num == '1':
        pass

    if num == '2':
        pass

    if num == '3':
        pass

print(f'프로그램을 종료합니다. 현재 잔액은 {balance}')
