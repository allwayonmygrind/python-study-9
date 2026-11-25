student = {'이름':'김파이', '학년':2, '전공':'컴퓨터공학', '점수': [90, 85, 77]}
print('이름 : '+ student['이름'])
print('전공 : '+ student['전공'])
print(student['점수'][1])
student['학년'] = 3
student['emaol'] = 'kim@py.com'
print(student)

# --------------------------------

army = dict(zip(['alpha', 'bravo', 'charlie', 'delta'],[10, 20, 30, 40]))
print(army['delta'])

#----------------------------------

camille = {'health': 575.6, 'health_regen': 1.7, 'mana': 338.8,
        'mana_regen': 1.63, 'melee': 125, 'attack_damage': 60,
        'attack_speed': 0.625, 'armor': 26, 'magic_resistance': 32.1,
        'movement_speed': 340}

print(camille['health'])
key = input('키 이름을 입력하세요 : ')
print(camille.get(key, '없는 항목!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!입니다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!B!R!E!A!K!Y!O!U!R!C!O!M!P!U!T!E!R'))