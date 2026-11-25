
# break 멈추기 #continue 계속진행(다음턴...으로 건너뛰기)

i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1

print('-'*26)

for i in range(100):
    print(i)
    if i==7 :
        break

for i in range(1, 11):
    if i == 5 :
        break
    print(i, end=" ")
print()

for i in range(1, 11):
    if i == 5 :
        continue # 건너뛰기, 5가 건너뛰어지니까 1 2 3 4 6 7 8 9 10
    print(i, end=" ")
print()

i = 0
while i < 10 :
    i = i+1
    if i%2==0:
        continue
    print(i, end=' ')

    # i = i+1 반복의 조건식이 거짓이 되는 케이스를 만드는 기준 변수의 변화... continue 앞 | 뒤 잘 구분할 것
print()

#메뉴 선택 반복 : 반복입력 q를 입력하면 종료

while True:
    cmd = input('명령어 입력(q 입력시 종료): ')

    if cmd == 'q':
        break
    if cmd =='':
        continue #빈 입력 무시
    print('입력한 명령어: ', cmd)


#for else    while else
#해당 반복이 break 없이 끝까지 다 돌면 else도 실행 / break 되면 노 실행
for n in [1,3,5,7]:
    if n%2 == 0:     #짝수면
        print('짝수발견')
        break
    # else 이것은 if의 else
else:        #for의 else
    print('짝수가 없다')