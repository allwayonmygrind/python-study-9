height, width = input("세로 , 가로 순으로 숫자 두개 공백으로 띄워서 입력 : ").split()
area = int(height)*int(width)
peri = int(height)/int(width) #둘레 구하는 법을 모르겠음....

print(f'넓이는 : {area}')
print(f'둘레는 : {peri}')

print('------------------')

kor, eng, math = map(int, input("국어, 영어, 수학 점수를 입력 : ").split(','))

score = int(kor)+int(eng)+int(math)

print(f'총점은 : {score}')

aver = int(score)/3

print(f'평균은 : {aver}')

print('----------------')

sec = input("초(second)를 입력하세요 : ")

hours = round(int(sec)/3600)
min = round(int(sec)/60)
second = round(int(sec)%60)

print(f'{hours}시간 {min}분 {second}초')

print('--------------------')

year, month, day = input('년 월 일 입력: ').split()
print(year, month, day, sep="/")