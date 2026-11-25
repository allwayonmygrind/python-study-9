age = int(input('나이를 입력하시오 : '))
price = None

if age < 8 :
    price = 0
elif 8 <= age <= 13:
    price = 650
elif 14 <= age <= 18:
    price = 1050
elif 19 <= age <= 64:
    price = 1350
else :
    price = 0


if price >= 1 :
    print(f'당신의 입장료는 {price}입니다.')
elif price == 0 :
    print(f'당신의 입장료는 무료입니다.')

#-----------------------

years = int(input('윤년 판별을 위한 년도를 입력하시오 : '))

if years%4 == 0 and years%100 != 0:
    print('윤년입니다')
elif years%400 == 0:
    print('윤년입니다')
else : 
    print('윤년이 아닙니다')

# ----------------------------

tranWallet = 9000
totalWallet = tranWallet-price

print (f'당신의 입장료 {price}을 당신의 교통카드 총 금액에 차감합니다. ')
print (f'당신의 교통카드 잔액은 : {totalWallet} 입니다')

# ----------------------

a, b, c = map(int, input('세 개의 정수를 입력하시오.').split())

if b <= a >= c :
    print(a)
elif a <= b >= c :
    print(b)
else :
    print(c)