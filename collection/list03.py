#리스트 조작


a = [30, 20 ,50 , 60, 10]

for i in range(len(a)) : 
    print(a[i], end=' ')
print()

for v in a:
    print(v, end=" ")
print()

for idx,value in enumerate(a):
    print(idx, value)
print()

i=0
while i <len(a):
    print(a[i], end=' ')
    i = i + 1
print()

#최소값, 최대값
smallest = a[0]
for v in a:
    if v <= smallest:
        smallest = v
print('최소값', smallest)

largest = a[0]
for v in a:
    if v >= largest:
        largest = v
print('최대값', largest)

# 함수 min max sum
print(min(a), max(a), sum(a))
# 10 60 170

# 평균    총합/갯수
print(sum(a)/len(a)) #34.0

#리스트 표현식 (리스트 컴프리핸션)
#[식 for 변수 in 반복이 가능한 객체]

b = [i for i in range(10)]
print(b)
#아래 명령어와 동일함
b = []
for i in range(10):
    b.append(i)
print(b)

c = [i*10 for i in range(1,11)]
print(c)
#아래와 같은 코드
# c=[]
# for i in range(1,11):
#     c.append(i*10)
# print(c)

# 조건붙이기 추가
#[식 for 변수 in \반복이 가능한 객체/ if 조건]
d = [i for i in range(10) if i % 2 == 0] #2로 나눈 나머지가 0인 것만 남겨놓겠다
print(d) #[0, 2, 4, 6, 8]
#아래와 같은 코드
# d = []
# for i in range(10):
#     if i%2 == 0:
#         d.append(i)
# print(d)

e = [x+5 for x in range(10) if x%2 == 1]
print(e)

#문자열 리스트
words = ['apple', 'banana', 'kiwi']
#upper = 대문자로 , lower = 소문자로
print(words[0].upper()) #APPLE
print(words[0].lower()) #apple

words_upper = [v.upper() for v in words]
print(words_upper) #['APPLE', 'BANANA', 'KIWI']

words_len = [len(v) for v in words]
print(words_len) #[5, 6, 4]

# map 모든 요소들에게 같은 함수 적용
words_len2 = list(map(len, words))
print(words_len2) #[5, 6, 4]

a= [1.1, 2.2, 3.3, 4.4]
b = list(map(int, a)) #실수형 숫자 int(1.1) -> 1 소숫점 날리면서 정수로 바꿈 \데이터손실
print(b) #[1, 2, 3, 4]

nums = list(map(str, range(5)))
nums2 = list(range(5))
print(nums) #['0', '1', '2', '3', '4'] 문자형으로 바뀜
print(nums2) #[0, 1, 2, 3, 4] 숫자형

#입력값 split -> map 적용
x = list(map(int, input('숫자 여러개 띄어쓰기로 입력 : ').split()))
print(x)

# 튜플
t = (30, 20, 50, 60, 10 ,40)
print(t.count(50), t.index(30)) # 1 0
print(min(t), max(t), sum(t)) #모두 정상 작동
t_even = tuple(i for i in range(10) if i % 2==0) #짝수인 값만 튜플로 만들어라
print(t_even) #(0, 2, 4, 6, 8)