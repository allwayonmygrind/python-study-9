scores = [88, 92, 75, 64, 95, 81, 70]

eit = [i for i in scores if i >= 80]

newList = sorted(scores, reverse=True)

print(f'최고점 : {max(scores)}, 최저점 : {min(scores)}, 평균 : {sum(scores)/len(scores):.2f}')

print(list(eit))

print(newList)

print('-------------------------')

longList = list(input('공백으로 구분된 단어들을 입력하시오 : ').split())

longestList = ''

fiveguys = []

for word in longList :
    if len(word) > len(longestList):
        longestList = word

for five in longList :
    if len(five) >= 5:
        fiveguys.append(five)

bigFive = [f.upper() for f in fiveguys ]

print(f'단어의 개수는 : {len(longList)}')
print(f'가장 긴 단어는 : {longestList}')
print(f'길이가 5 이상이면 대문자가 됨 : {bigFive}')

print('-----------------------------')

cart = []

while True:
    command = input('명령어를 입력하세요 : ').split()

    if not command:
        continue

    if command[0] == 'add':
        if command[1] in cart:
            print(f'"{command[1]}"는 이미 담긴 상품입니다.')
        else :
            cart.append(command[1])
            print(f'물품 "{command[1]}" 이 추가되었습니다.')

    elif command[0] == 'del':
        if command[1] not in cart:
            print(f'"{command[1]}"는 없는 상품입니다.')
        else :
            cart.remove(command[1])
            print(f'물품 "{command[1]}" 이 삭제되었습니다.')

    elif command[0] == 'q':
        for idx, value in enumerate(cart):
            print(f'장바구니 목록 | 번호 : {idx} , 물품 : {value}')
        break

    