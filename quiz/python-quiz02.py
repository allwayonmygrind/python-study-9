url = 'https://www.python.org/downloads'
print(url[0:5])
print(url[8:22])
print(url[-9::])

n = [-32, 5, 2, -10, 55, 7, 9, 0]
print(n[1::2])
print(n[-3::])
print(n[::-1])

days = input('날짜를 입력해주세요')

years = days[0:4]
month = days[4:6]
dayday = days[6::]
print(f'{years}년 {month}월 {dayday}일')

year = (2021, 2022, 2023, 2024, 2025, 2026)
population = (10249679, 10195318, 10143645, 9994195, 9886021, 9810000)

lastThirdYears = year[-3::]
lastThirdPopu = population[-3::]

print(f'최근 3년의 연도{lastThirdYears}에 따른 인구수는 : {lastThirdPopu}')
