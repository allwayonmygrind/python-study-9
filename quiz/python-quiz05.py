total = 0

num = int(input('구구단을 할 단을 입력하시오'))

for i in range(1, 10):
    print(f'{num} x {i} = {num*i}')

# -----------------

sum = 0

score = int(input('마지막 수를 입력하시오 : '))

jjak = 0
hole = 0

for i in range(1, score) :
    if i%2 == 0:
        jjak += i
    elif i%2 != 0:
        hole += i

print(f'짝수의 합은 : {jjak}')
print(f'홀수의 합은 : {hole}')

#----------------------------

x = [49, -17, 25, 102, 8, 62, 21]

for i in x:
    i *= 10
    print(i, end = " ")

# ----------------------------
print('\n')
    
wallet = 13000

while wallet >= 1350:
    wallet = wallet-1350
    print('남은 잔액 : ', wallet)
    # if wallet < 1350 :
    #     break