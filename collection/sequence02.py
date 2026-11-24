

#슬라이스

# [시작인덱스:끝인덱스:증가폭]
# exclusive

l = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

print(l[0:4]) #0:4까지 짤라서 짜른 부분만 보여주겠다 [0, 10, 20, 30]
print(l[2:7])
print(l)
print(l[0:len(l)])

print(l[0:len(l):2]) #0 2 4 6 8
print(l[0:10:3]) #0 3 6 9

print(l[-7:-2])
print(l[0:-2])

#인덱스 생략
print(l[:7]) # 처음부터 6까지 (<7)
print(l[3:]) # 3인덱스부터 끝까지
print(l[:]) #전체 (복사)
l2 = l #얕은복사
l2 = l[:] #깊은복사

print(l[::2]) #처음부터 끝까지 2씩 증가
print(l[::-1]) # 정렬을 거꾸로 뒤집는 용도로 사용

# 튜플, range, str 슬라이스
t = (1,2,3,4,5)
print(t[0:3])
print(range(10)[3:7]) #0부터 9까지 만들어내고 3인덱스부터 7까지 짤라내고 6까지 나타냄 3,4,5,6

s = 'Hello, world!'
print(s[0:5])
print(s[5:])
print(s[::-1]) #문자열 뒤집기

jumin = '991201-1234567'
print(jumin[0:6])#앞자리
print(jumin[7:])#뒷자리
print(jumin[7])#성별숫자

# 슬라이스 활용 값 바꾸기

a=[10, 20, 30, 40, 50]
a[1:3] = ['a', 'b']
print(a)

a[1:3]=['x']
print(a)

a + [60, 70, 80]
print(a)
a.append(90) #맨 뒤에 90 추가됨
print(a)

del a[0]
print(a)
del a[1:4]
print(a)