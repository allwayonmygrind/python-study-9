

s ='Hello, world!'

#문자 바꾸기 (대체하기) replace

print(s.replace("world", "Good")) #원본은 유지 , 비파괴적임
print(s) # Hello, world!

s = s.replace("world", "Good") #원본에 덮어씌움
print(s) # Hello, Good!

#분리 / 합치기 split join
words = 'apple kiwi banana melon'.split()
print(words)

print('apple,kiwi,banana,melon'.split(','))

#구분자.join(리스트)
print('-'.join(words))#apple-kiwi-banana-melon
print('/'.join(words))#apple/kiwi/banana/melon
print(''.join(words)) #applekiwibananamelon

#대소문자
print('hello'.upper())
print('GREAT'.lower())
print('hello great'.title()) #Hello Great        모든 단어 앞 대문자로
print('hello great'.capitalize()) #Hello great  맨 앞 대분자로

#공백제거 (입력값 정리)
text = ' wonderful '
print('[', text.strip(), ']') # .strip은 공백을 없애줌 띄어쓰기나 들여쓰기
print('[', text.lstrip(), ']')
print('[', text.rstrip(), ']')
print('[', '. this us text!! '.strip('.!'), ']') #[  this us text!!  ] 앞에 . 사라짐
#strip은 무조건 양쪽 끝에 있는 것만 지우기 때문에 !는 안사라짐

# 문자열 폭 정렬
print('[' 'python'.ljust(10) ,']') #10칸을 차지 하겠다
print('[' 'python'.rjust(10) ,']')
print('[' 'python'.center(10) ,']')
print('[' 'python'.zfill(10),']')    #f (2:0>5)
print('2'.zfill(2))

print('[', 'python'.ljust(10, '*') ,']')

#문자 찾기
s = 'apple pineapple'
print(s.find('pl')) #앞에서부터 찾아서 가장 먼저 찾은 위치를 돌려줌
print(s.rfind('pl')) #오른쪽에서부터 찾기
print(s.find('ex')) #없으면 -1 if 찾은결과 == -1: 없구나~
print(s.index('pl')) #찾은 인덱스
# print(s.index('ex')) #못찾으니 오류
print(s.count('p')) #갯수세기

#시작 끝 확인
file_name  = 'report.xlsx'
print(file_name.startswith('report')) #True
print(file_name.endswith('xlsx')) #True
print(file_name.endswith('pptx')) #False ppt 파일이 아니구나

#문자 타입 종류 판단
print('1234'.isdigit()) 
print(int('1234'))
print('12q34'.isdigit()) #False 숫자형태가 아님
# print(int('12q34')) 오류가 남 q는 int로 바꿀 수 없어서

print('1234'.isalpha()) # 알파벳으로 이루어져있느냐 False
print('abcd'.isalpha()) # True

print('abcd'.isalnum()) #True
print('1234'.isalnum()) #True
print('1234abcd!@#$'.isalnum()) #False
print('1234abcd'.isalnum()) #True

# 메소스 체이닝 (이어붙여서 수행)
raw = '  Hello, Python  '

raw = raw.strip() #띄어쓰기 없애기
raw = raw.lower() #소문자로 바꾸기
raw = raw.replace('python', 'world') #python을 world로 바꾸기

print(raw)

raw2 = '  Hello, Python  '
raw2 = raw2.strip().lower().replace('python', 'world2') #이렇게 한번에도 가능
print(raw2)

email = input('이메일 : ').strip().lower() #공백제거, 소문자로
print(email)
# s =email.split('@)
# s[0]  s[1]
user_id, domain = email.split('@')
print(user_id, domain)