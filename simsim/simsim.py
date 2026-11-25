
# ■ 변수와 연산
# 1. 다음 코드를 실행한 뒤 n의 값은?
# n = 50
# n -= 8
42
# # n //= 4
12
# # n *= 3
150


# 2. 다음 코드의 출력 결과는?
# p, q, r = 'a', 'b', 'c'
# p, q, r = r, p, q
p = 'c'
q = 'a'
r = 'b'
# print(p, q, r)
c a b

# 3. 다음 코드의 출력 결과는?
# k = m = 5
# k += 1
# print(k, m)
6 , 5

# ■ 입력: input, split, map

# 4. 다음 코드의 출력 결과는?
# y, mo, d = map(int, "2026-11-24".split('-'))
# print(mo + d)
35

# 5. print(len(" 사과 배 감 ".split())) 의 결과는? (공백 개수에 주의)
3

# 6. 두 정수를 콤마로 입력받아(예: 7,3) 아래처럼 출력하는 코드를 쓰세요.
# 7을 3로 나누면 몫 2, 나머지 1
sev, thr = 7, 3
neck = sev//thr
dust = sev%thr
print(f'{sev}를 {thr}로 나누면 몫은 : {neck} 나머지는 : {dust}') 


# ■ 출력: print, sep, end, f-string

# 7. 다음 두 줄의 출력 결과는?
# print('A', 'B', sep='*', end='#')
A*B#C
# print('C')
C

# 8. print(3, 4, sep='\n', end='끝\n') 의 출력 결과를 줄 단위로 쓰세요.
3
4끝


# 9. 다음 두 줄의 출력 결과는?

# print(f'{7/3:.2f}')
2.33
# h, mi = 9, 5
# print(f'{h:02d}:{mi:02d}')
09:05


# 10. yy, mm, dd = 2026, 1, 7 일 때 sep을 사용해 2026.01.07 로 출력하는 코드를 쓰세요. (f-string 사용 금지)
print(yy,mm,dd, sep='.')

# ■ bool, 비교·논리 연산자

# 11. print(3 < 5 < 4, not (3 == 3.0)) 의 결과는?
False, False

# 12. print(0 or 'B', 'A' and 'C') 의 결과는?
B C


# 13. print(bool('0'), bool(0.0), bool([0])) 의 결과는?
True , False, True

# 14. t = 15 일 때 print(t % 2 == 1 and t > 10) 의 결과는?
True

# ■ 문자열
# 15. 다음 코드의 출력 결과는?
# s = 'ab' * 2 + 'c'
s = ababc
# print(s, len(s))
ababc 5


# 16. 다음 두 줄의 출력 결과는?
# print('C:\\temp\\new')
C:\temp\new
# print(len('가\t나\n'))
가탭나줄
4


# 17. print('py' in 'Python', 'Py' in 'Python') 의 결과는?
false True

# ■ 리스트, 튜플, range

# 18. print(list(range(20, 5, -5))) 의 결과는?
[20, 15, 10]
# 19. v = 1, 일 때 print(type(v), len(v)) 의 결과는?
int ine

# 20. 다음 코드의 출력 결과는?
# nums = [5, 6, 7]
# a, b, c = nums
# nums[0] = 50
# print(a)
5

# ■ 시퀀스 공통 기능
# 21. print(len([1, [2, 3], 'four'])) 의 결과는?
3

# 22. w = 'banana' 일 때 print(w[1] + w[-2] + w[3]) 의 결과는?
ana

# 23. print(list(range(1, 4)) + [4] * 2) 의 결과는?
[1,2,3,4,4] 

# ■ 슬라이스

# ※ 24~25번은 data = [3, 6, 9, 12, 15, 18, 21] 을 씁니다.

# 24. print(data[1:-1:2]) 의 결과는?
[6, 12, 18]

# 25. print(data[::-2]) 의 결과는?
[21, 15, 9, 3]

# 26. code = 'A2026-0815-K' 에서 '0815' 를 "음수 인덱스"로 슬라이스해서 꺼내는 코드를 쓰세요.
print(code[-6:-2])

# 27. 다음 코드의 출력 결과는?
# m = [1, 2, 3, 4, 5]
# m[1:4] = ['x']
# print(m)

# ■ 딕셔너리
# 28. 다음 코드의 출력 결과는?
# sc = {'kor': 80, 'eng': 75}
# sc['eng'] += 10
# sc['math'] = sc.get('math', 0) + 90
# print(sc)
# 29. 다음 코드의 출력 결과는?
# d = {1: 'a', True: 'b', 'x': 'c', 'x': 'd'}
# print(len(d), d[1])
# 30. 다음 코드의 출력 결과는?
# c = dict(zip(['r', 'g', 'b'], [255, 128, 0]))
# c['b'] += 64
# print(c, 'a' in c)