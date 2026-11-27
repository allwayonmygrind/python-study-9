scores = [
    ['김철수', 90, 85, 77],
    ['이영희', 72, 95, 88],
    ['박민수', 65, 70, 92],
    ['최지우', 98, 89, 94],
]
#(이름, 국어, 영어, 수학)

for a, b, c, d in scores:
    total = sum([b, c, d])
    avg = total/3
    print(f'{a} | 총점 : {total}, 평균 : {avg:.2f}')

print('----') # -----

korTotal = 0
engTotal = 0
mathTotal = 0


for i in scores:
    korTotal += i[1]
    engTotal += i[2]
    mathTotal += i[3]


korAv = korTotal/len(scores)
engAv = engTotal/len(scores)
mathAv = mathTotal/len(scores)

print(f'과목별 평균 | 국어 : {korAv}, 영어 : {engAv}, 수학 : {mathAv}')

print('-----') # ----

maxTotal = 0
potg = ''

for i in scores:
    total = sum(i[1:])
    if total > maxTotal:
        maxTotal = total
        potg = i[0]

print(f'총점이 가장 높은 학생은 : {[potg]}')

print('----') # ----

a = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]

for a, b, c, d in a:
    print(a, b, c, d)
    