#리스트 중첩
#2차원 리스트

#2차원 행, 열

a = [
        [10,20],
        [30,40],
        [50,60]
    ]

print(a) #[[10, 20], [30, 40], [50, 60]]

print(a[1]) #[30,40]

print(a[1][0]) #30
a[0][1] = 99

print(a) #[[10, 99], [30, 40], [50, 60]]


b = [
        [10,20],
        [30,40],
        [50,60]
    ]

#반복문으로 2차원 리스트 출력

for i in range(len(b)):    #3 : 0 1 2 
    for j in range(len(b[i])):
        print(b[i][j], end=' ')
    print() 
# 10 20 
# 30 40 
# 50 60 

for row in b :                  #반복문 1차 반복 [10,20] 배정 ,2차 반복 [30,40] ... 차례대로
    for v in row :
        print(v, end = ' ')
    print()
print('-'*50)
# 10 20 
# 30 40 
# 50 60 

for x, y in b:
    print(x, y)
print('-'*50)
# 10 20
# 30 40
# 50 60

# 2차원 리스트 생성
# [[], [], []]

c = []
for i in range(3):
    temp = []
    for j in range(2):      # []
        temp.append(j)
    # temp = [0, 1]
    c.append(temp)
print(c) #[[0, 1], [0, 1], [0, 1]]

d = [i for i in range(3)]
print(d) #[0, 1, 2]

e = [[j for j in range(2)] for i in range(3)]
print(e) #[[0, 1], [0, 1], [0, 1]]

f = [ [0] * 2 for i in range(3)]
print(f) # [[0, 0], [0, 0], [0, 0]]

students = [['john','C', 19], ['maria', 'A', 25], ['andrew', 'B', 7]]
print(sorted(students)) # [['andrew', 'B', 7], ['john', 'C', 19], ['maria', 'A', 25]] 제일 앞에 있는 거 기준 정렬
print(sorted(students, reverse=True)) #[['maria', 'A', 25], ['john', 'C', 19], ['andrew', 'B', 7]]
# 특정 위치의 열을 기준으로 정렬

print(sorted(students,key=lambda s: s[1] )) #1인덱스 위치 기준으로 정렬
#[['maria', 'A', 25], ['andrew', 'B', 7], ['john', 'C', 19]]
print(sorted(students,key=lambda s: s[2] )) #2인덱스 위치 기준으로 정렬
#[['andrew', 'B', 7], ['john', 'C', 19], ['maria', 'A', 25]]

#2차원 리스트 복사
a = [[10,20],[30,40]]
b = a

print(a, b) #[[10, 20], [30, 40]] [[10, 20], [30, 40]]
a[0][0] = 99 # a와 b의 값이 똑같이 바뀜 얕은 복사라서
print(a, b) #[[99, 20], [30, 40]] [[99, 20], [30, 40]] 

print('-'*50)
a = [[10,20],[30,40]]
b = a.copy()

print(a, b) #[[10, 20], [30, 40]] [[10, 20], [30, 40]]
a[0][0] = 99
print(a, b) #[[99, 20], [30, 40]] [[99, 20], [30, 40]]

import copy
print('-'*50)
a = [[10,20],[30,40]]
b = copy.deepcopy(a)

print(a, b) #[[10, 20], [30, 40]] [[10, 20], [30, 40]]
a[0][0] = 99 #깊은 복사 당해서 a 값만 
print(a, b) #[[99, 20], [30, 40]] [[10, 20], [30, 40]] #새로운 배열