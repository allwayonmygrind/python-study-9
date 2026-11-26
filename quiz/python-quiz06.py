height = int(input('높이를 입력하시오 : '))

for i in range(height):                            
    for j in range(height):              
        if j >= i : 
            print('*', end='')
    print()
print()

print ('------------------------')
for i in range(height):
    for j in range(height-1-i):
        print(' ', end='')

    for j in range(i*2+1):
        print('*', end='')

    print()

print ('------------------------')

for i in range(height):
    for j in range(i):
        print(' ', end='')

    for j in range(2*(height-i)-1):
        print('*', end='')

    print()

print ('------------------------')

for i in range(height):
    for j in range(height-1-i):
        print(' ', end='')

    for j in range(i*2+1):
        print('*', end='')
    print()

for i in range(1, height):
    for j in range(i):
        print(' ', end='')

    for j in range(2*(height-i)-1):
        print('*', end='')

    print()