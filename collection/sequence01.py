

# sequence 시퀀스

#각 자료형에 사용되는 기능

l = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
t = (11, 22, 33, 44)
r = range(0, 10, 2)# 0 2 4 6 8 
s = "Hello, world!"

#in, not in 내부에 포함인가 or 미포함인가를 식별
print(30 in l)
print(100 in l)
print(44 in t)
print(12 in r)
print(2 in r)
print('H' in s)
print('W' in s)
print('abc' not in s)

# + 연결하기
print(l + [100, 110])
print(l)
print(t + (55, 66))
print(s + "good day")
# print(r + range(10, 16, 2 )) #range + 불가
print(list(r)+ list(range(10,16,2))) #리스트 변환후 더하기 가능

# * 연산 반복하기
print([1,2]*3) # [1, 2, 1, 2, 1, 2]
print(('a', 'b')*3) #('a', 'b', 'a', 'b', 'a', 'b')
print('-' * 50) #--------------------------------------------------

# 해당 요소의 길이 len()
print(len(l))
print(len(t))
print(len(r))
print(len(s))

# 인덱스 : 0 ~
print(l[2])
print(t[1])
print(r[3])
print(s[9]) #문자열에서의 인덱스는 해당위치의 문자 하나를 제공

# 음수 (-) 인덱스 : -1 -2 -3 ..... 맨뒤에서부터
print(l[-1]) #90
print(s[-1]) #! 

# print(l[20]) #인덱스를 벗어난 인덱스는 안됨 #list index out of range


# 리스트만 가능한 기능
l[2]='변경'
print(l)

del l[2]
print(l)#해당 위치에 있는 값을 지움

print(s[2])
# s[2] = '?'  문자열 인덱스는 변경 불가
print(s[2])