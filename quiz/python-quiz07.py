import random
dice = random.randint(1, 100)

count = 0

while True:

    if count >= 7 :
        print(f'정답은 : {dice}였습니다 정진하세요')
        break

    player = int(input('1부터 100사이에서 랜덤한 숫자를 맞추시오!!!!!! : '))

    if player < 1 or player > 100 :
        print('잘못된숫자다!!!!!!!!!!!!정신단디해라!!!!!!!!!')
        print('')
        continue

    count += 1
    
    if player > dice :
        print('Down')
        print('')
    
    elif player < dice :
        print('Up')
        print('')

    elif player == dice :
        print(f'정답입니다!!!!! 짝짝스 총 {count}회 만에 맞추셨습니다!!!!')
        break

    