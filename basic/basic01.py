
print('basic01.py')

# 주석
# 앞에 #을 붙이면 그 라인은 주석이 된다.

#여러줄 주석

"""
주석이구요
"""

print("hello") #뒤에 #부터 다시 주석

# 2. 세미콜론
# 세미콜론 안붙여도 오류나지 않음
print('hello');
print('hello1')
print('hello2')
print('hello3'); print('hello4') # 한줄에 여러문장 사용시에 구분을 위해 ;를 넣어야 오류가 안남

# 3. 들여쓰기 (indent)
# 구역 범위를 나타낼 떄 사용하던 {} 대신에 들여쓰기를 사용
#들여쓰기는 Tab 눌러서 적용 (공백 4칸)

print('들여쓰기2')
    #print("들여쓰기3") 의미없이 들여쓰기 X

x = 10
print(x)
if x == 10:
    print("이거슨 10이오")
    #들여쓰기 내부 범위

print("여기는 if문 밖")

# 4. 코드 블록
if x > 5:
    print('bigger than 5')
    if x > 8:
        print('bigger than 8')
    print('x>5 블록')

if x > 100:
    pass #if 들여쓰기 안에 아무것도 안할꺼라면 pass를 적어야 오류가 안남

print("if문 다음")