
#리스트와 튜플

#리스트(list) : 대괄호 [] 여러값 묶어서 저장

a = [12,34,67,22]
print(a)
print(type(a)) #<class 'list'>

#자료형 상관없이 함께 저장 가능
person = ['홍길동', 25, 175.5, True]
print(person)

#빈리스트
b = []
c = list()
print(b,c)

#range() 활용 리스트 만들기
print(list(range(10))) # 0부터 9까지
print(list(range(5, 12))) # 5부터 11까지 값  (5 <= n < 12)
print(list(range(0, 20, 2))) # 0부터 18까지 2씩 증가하는 값
print(list(range(10, 0, -1))) # 10부터 1까지 1씩 감소하는 값


#튜플 : 소괄호 () 로 묶어서 값을 저장, 생성 후 값 변경이 불가 (Like const)
t = (11,22,33,44)
print(t)
print(type(t)) # <class 'tuple'>

t2 = 11, 22, 33 #튜플로 저장됨
print(t2)

t3 = (38)   #그냥 정수
print(t3)   
t4 = (38,)  #튜플로 인식
print(t4)

#리스트 값 변경 가능, 튜플은 불가능
print(a[1])
print(t[2])
a[1] = 99
print(a[1])
# t[2] = 88 # 튜플은 값을 변경하는 것을 허용하지 않는다 'tuple' object does not support item assignment

# a:list t:tuple
#list tuple 변환
print(tuple(a))
print(list(t))

print(list('Hello')) #문자열을 분해해서 한글자씩 리스트로 ['H', 'e', 'l', 'l', 'o']

x, y, z = [10, 20, 30]
q, w = (40, 50)

print(x, y, z, q, w) # 10 20 30 40 50