#在字典中，你可以通过使用符号构成 d = {key : value1 , key2 : value2} 这样的形式，来成
#对地指定键值与值
ab={
    'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'
    }
print('Swaroop\'s address is',ab['Swaroop'])

del ab['Spammer']

print('\nThere are {} comtacts in the address-book\n'.format(len(ab)))

for name,address in ab.items():
    print('contact {} at {}'.format(name,address))

#添加一对键值-值配对
ab['Guido']='guido@python.org'

if 'Guido' in ab:
    print('\nGuido\'s address is ',ab['Guido'])
