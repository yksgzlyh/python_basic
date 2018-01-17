number=23
running=True
while running:
    guss=int(input('Enter a number: '))
    if guss==number:
        print('guss right')
        running=False
    elif guss<number:
        print('lttle')
    else:
        print('longer')
else:
    print('Over')

print ('Done')
