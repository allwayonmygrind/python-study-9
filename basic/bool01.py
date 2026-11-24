
# 불 자료형 (bool) boolean 참 / 거짓
# True | False (첫글자 대문자)

print(True, False)
print(type(True))

#비교연산자 -> 결과가 True | False
print( 10 == 10 )
print( 10 != 10)
print( 10 > 20)
print( 10 < 20)
print( 10 <= 10)
print( 10 >= 10)

# 문자열 비교
print('Python' == 'Python')
print('Python' == 'python')
print('Python' != 'python')


print('------------')
# 값 ==   객체 비교는 is

n1 = 1
n2 = 1.0
print(n1 == n2)
print(type(n1) == type(n2))

# print (n1 is n2)
print(type(n1) is type(n2))

x = None

print(x == None)
print(x is None) # None 비교는 is가 권장된다 함

# 논리연산자 and or not
print(True and True) # &&
print((1==1) and (2>1)) # ||
print(False or True)
print(not True) # !

age = 25
print( age >= 20 and age < 30)
print( 20 <= age <30 ) #파이썬은 아래처럼 한번에 적어도 허용해준다

print ( age > 10 or age < 100)


print('---------------')
# 정수, 실수, 문자열 -> bool 
print(bool(1), bool(0)) # 0을 False라 인식
print(bool('a'), bool(' '), bool("")) #빈문자열을 False라 인식
print(bool([]), bool([1,2,3])) # 빈리스트를 False

# && ||
print(False and 'abc')
print(True  and 'abc') #앞의 값이 참이면 뒤 값 출력 거짓이면 거짓을 출력
print(False or 'def') # def가 출력됨