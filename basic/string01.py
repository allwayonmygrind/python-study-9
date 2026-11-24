
#큰 따옴표 작은 따옴표 둘다 가능
hello = "hello, world!"
hi = '안녕하세요'

print(hello)
print(hi)
print(type(hi))

#작은 따옴표 넣고싶으면 큰 따옴표로 감싸기
s1 = "my name's ..."
#큰 따옴표도 반대로 똑같이
s2 = 'hi"hello"'
#escape 문자 \ -> 큰 작은 따옴표앞에 붙이면 ㄱㅊ아짐
s3 = '큰"따옴표 작은\'\"따옴표'

print(s1)
print(s2)
print(s3)

#여러줄 문자열
s4 = '''
    여러줄
    문자열을
    나타낼 때
    사용할 수 있다
    '''
print(s4)

s5= """
    여러줄
    문자열을
    나타낼 때 " 큰따옴표도 가능
"""
print(s5)

#이스케이프 문자
print('줄바꿈\n문자')
print('탭 띄어쓰기\t문자')
print('역슬래시 \\ 문자')

#문자열 연산
a = 'hello'
b = 'world'

print(a+b)
print(a + ' ' + b)
print(a, b, sep=" ")
print( a * 3) #반복 의미
print('-' * 30) #구분선 역할

#문자함수
print(len(a))
print(len('글자길이찾아봐라'))
print('ll' in a) #ll이 a에 있느냐 포함돼 있느냐
print('ll' in b)
print('ll' not in b)

num = '123'
print(int(num) + 123)
print(str(123) + '456')