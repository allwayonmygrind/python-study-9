
#for 반복문 range 0~4

# for 변수 in range():

for i in range(5):        # 0 1 2 3 4
    print(i)

for i in range(3, 10):
    print(i , end=' ')
print()

for i in range(0, 20, 2): #0부터 20이전 까지 2씩 증가함 0 2 4 6 8 10 12 14 16 18
    print(i, end=' ')
print()

for i in range(10, 0, -1): #10부터 0전까지 1씩 감소 10 9 8 7 6 5 4 3 2 1
    print(i, end=' ')
print()

for i in reversed(range(0, 10)):       # 순서를 뒤집어서 출력함 9 8 7 6 5 4 3 2 1
    print(i, end=' ')
print()

#입력 활용
# count = int(input('횟수입력:'))
# for i in range(count): 
#     print(i , end=' ') # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# print()

#합계 1 ~ 100 합계
sum = 0
for i in range(1, 101):
    sum = sum+i
print('총합', sum) #5050

# 반복문 사용, 구조 자료형으로 사용가능 : 리스트, 튜플 , 문자열 시퀀스
fruits = ['사과', '바나나', '딸기']
for fruit in fruits:
    print(fruit)

for ch in 'Python':
    print(ch , end=' ')
print()

for i in range(len(fruits)):
    print(i, fruits[i])

for idx, item in enumerate(fruits):    #인덱스, 값 을 둘다 돌려준다
    print(idx, item)

# 구구단 2단 출력
for i in range(1, 10): # 1 2 3 4 5 6 7 8 9
    print (f'2 x {i} = {2*i}')

# 안쓰는 값 _
for _ in range(10):
    print('*', end='')
print()