# 변수

# 변수명 = 값

x = 10
y = 3.14
name = "홍길동"
is_ok = True       #python은 변수명에 $ 사용불가

print(x)
print(y)
print(name)
print(is_ok)
print(type(x), type(y), type(name), type(is_ok))

# 변수명
# 영문, 숫자, _ 특수문자 가능 / 숫자시작 불가
# 대소문자 구분 (Name, name은 다른 변수로 봄)
# 키워드 사용불가 (if문 for문 class문)
#의미있는 단어로 표현

#변수명을 짓는 스타일 
#자바,js -> 카멜케이스 -> userName
#Python -> 스네이크 케이스 -> user_name
#둘다 사용가능하나 업계에서 일반적으로 이렇게 사용함
user_name = "파이썬"
print(user_name)
userName = "파이썬"
print(userName) 

# 숫자형 n ---> n = 10, n = 20, n="문자" 다른 언어들은 자료형이 문자면 숫자가 안돼고 숫자면 문자로 바뀌면 오류가 나는데
# 파이썬은 자료형이 바뀌어도 괜찮다

x = 20
print(x)
x = '문자열 저장'
print(x, type(x))

a, b, c = 10, 20, 30
print(a, b, c)
d = e = f = 9
print(d, e, f)

# 두 변수의 값 바꾸기
print(a, b)

a, b=b, a #b값을 a에 저장하고 a값을 b에 저장 #서로 값 바꾸기
print(a, b)

del d 
#print(d) #NameError: name 'd' is not defined

# 빈 변수 : none
z = None
print(z)

#변수 계산
a = 10
b = 20
c = a + b
print(c)
c = a + a +b + b
print(c)

a = a + 5
a += 5
a -= 3
a *= 2
a //= 5

x = -10
print(-x)