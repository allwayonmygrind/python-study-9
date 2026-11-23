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