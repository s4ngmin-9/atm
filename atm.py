# balance : 초기 잔액을 설정하는 변수를 초기화해주세요
# 금액은 여러분 마음대로 설정해주세요

# 사용자로부터 atm 기계에 사용 목적에 맞는 기능을 선택할 수 있도록
# 기능 입력을 받는 기능을 구현해주세요


balance = 100000000

receipts = []

while True:
    num = input("사용하실 기능을 선택해주세요 (1. 입금, 2. 출금, 3. 명세표 출력, 4. 종료) : ")

    if num == '4':  # 종료
        break

    if num == '1': # 입금 기능 구현 > feat/deposit
        deposit_amount = int(input('입금할 금액을 입력해주세요. : ')) # str : 5000 > int > int : 5000
        balance += deposit_amount # balance = balance + deposit_mount
        print(f'입금하신 금액은 {deposit_amount} 원이고, 현재 잔액은 {balance} 원 입니다.')
        receipts.append(('입금', deposit_amount, balance))

    if num == '2':
        withdraw_amount = int(input('출금할 금액을 입력해주세요. :'))
        withdraw_amount = min(balance, withdraw_amount)
        balance -= withdraw_amount
        print(f'출금하신 금액은 {withdraw_amount} 원이고, 현재 잔액은 {balance} 원 입니다.')
        receipts.append(('출금', withdraw_amount, balance))

    if num == '3':
        if receipts:
            for i in receipts:
                print(f'{i[0]}: {i[1]} 원 | 잔액: {i[2]} 원')
            else:
                print("영수증 내역이 없습니다.")
            

print(f'프로그램을 종료합니다. 현재 잔액은 {balance} 원 입니다.')
