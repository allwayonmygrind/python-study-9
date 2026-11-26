

#리스트 조작

a = [10,20,30]
a.append(40)

print(a)

# 함수 / 메소드
# 특정 객체에 속한 함수 : 메소드

a.append([100,200])
print(a[4])
print(a[4][0])
print(a[4][1])

# [10, 20, 30, 40, [100, 200]]
print(len(a)) #리스트의 길이

b = [1, 2, 3]
# b.append([4,5])
b = [1,2,3] + [4,5]
#b = [1,2,3,4,5]

#리스트를 연결해서 확장
b.extend([6,7,8])
print(b) # [1, 2, 3, 4, 5, 6, 7, 8]

#특정위치에 추가 insert
c = [10,20,30]
c.insert(1, 500) # 1인덱스 위치에 500추가 
print(c) #[10, 500, 20, 30]

c.insert(0, 100) # 0인덱스 위치에 100추가 
c.insert(len(c), 100) # 맨뒤에 100추가 
print(c) # [100, 10, 500, 20, 30]

#리스트 요소 삭제
d = [10, 20, 30]
print(d)
print(d.pop()) #제일 뒤에 요소를 삭제하면서 return 하기 떄문에 print에 적어도 적용됨(이 코드에서만 작용하는 1회용 X)
#pop의 값은 삭제하려는 리스트의 결과가 아니라 삭제한 값의 결과 즉 30이 나옴
print(d)
print(d.pop(0)) #pop(index) 제일 앞 요소 삭제하면서 return

#값으로 요소 삭제
e= [10,20,30,40,20]

e.remove(30) #인덱스가 아닌 값을 찾아서 지운다.
print(e) #[10, 20, 40, 20]
# e.remove(50) 없는 값이기 때문에 error 뜸

e.remove(20) #앞에서부터 찾아서 처음 나오는 값 한개만 삭제
print(e) #[10, 40, 20]

# 검색

e= [10,20,30,40,20]

print(e.index(30)) #해당 값이 위치한 인덱스를 반환 > 2 가 나옴
# print(e.index(50)) 이것 역시 없다고 오류가 남
print(e.count(20)) #해당 값의 개수를 찾는다 > 2 (20)이 두개이기 때문

#뒤집기
e.reverse() #리스트가 반대방향으로 뒤집힌다
print(e) #[20, 40, 30, 20, 10]

#정렬
e.sort() #리스트를 오름차순으로 정렬
print(e) #[10, 20, 20, 30, 40]

e = [1, 82, -6 ,213 , 21, 8, 4]
e.sort(reverse=True) #리스트를 내림차순으로 정렬 
print(e) # [213, 82, 21, 8, 4, 1, -6]
e.sort(reverse=False) #False는 기본값 오름차순으로 정렬이다
print(e) #[-6, 1, 4, 8, 21, 82, 213]

# sorted() vs sort()
q = [7,2,-1,12,5,8,6,2]
#q.sort() 리스트를 그대로 정렬
sorted(q) #매개변수로 받아서 정렬함 / 정렬해서 정렬된 리스트를 반환, 새로운 리스트로 반환하고 (원본은 유지)
w = sorted(q)
print(q) # [7, 2, -1, 12, 5, 8, 6, 2]
print(w) #[-1, 2, 2, 5, 6, 7, 8, 12]
e = sorted(q, reverse=True)
print(e) #[12, 8, 7, 6, 5, 2, 2, -1]

q.sort() #원본반영, 원본을 바꿈
print(q) #[-1, 2, 2, 5, 6, 7, 8, 12]

print('-----------')

print(sorted(q, reverse=True))
print(e.sort()) #None e.sort() 내부적으로 정렬을 할 뿐, 반환이 없음

#모든 요소 삭제
e.clear()
print(e) #[] 빈 리스트

#리스트 복사
a = [1,2,3,4] #참조타입변수 주소....
b = a         #실제 복사가 일어난 건 아님
print( a == b) #True 새로운 배열을 만든게 아닌 주소를 복사했기 때문
print( a is b) #True

a[0] = 99 # a, b 둘다 바뀐 것으로 보임
print(a)
print(b)

a = [1,2,3,4]
b = a.copy()
c = a[:] #리스트에 있는 요소 전체에 접근 
d = a[::-1] #모든 요소를 거꾸로

a[0] = 99

print(a, b, c, d)
#[99, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4] [4, 3, 2, 1]
#      a            b             c           d

print( a == b) #False
print( a is b) #False

a[0] = 99

print(a, b, c, d)