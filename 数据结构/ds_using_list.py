#This is my shopping list
'''
我们通过列表对象中的 append 方法向列表中添加一个对
象

我们列表的 sort 方法对列表进行排序。在这里要着重理解到这一方法影响到的是列
表本身，而不会返回一个修改过的列表
'''
shoplist=['apple','mango','carrot','banana']
print('I have ',len(shoplist),' items to purchase')
print('These items are :',end='')

for item in shoplist:
    print(item,end=' ')
    
print('\n I also have to buy rice.')
shoplist.append('rice')
print ('My shoplist is now',shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is',shoplist)

print('The first item i will buy is',shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print('I bought the ',olditem)
print('My shopping list is now ',shoplist)
