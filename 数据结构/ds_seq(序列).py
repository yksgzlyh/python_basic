shoplist=['apple','mango','carrot','banana']
name='swaroop'

#索引
print('Item 0 is ',shoplist[0])
print('Item 1 is ',shoplist[1])
print('Item 2 is ',shoplist[2])
print('Item 3 is ',shoplist[3])
#反向第一个
print('Item -1 is ',shoplist[-1])
#反向第二个
print('Item -2 is ',shoplist[-2])

print('Character 0 is ',name[0])

#序列
print('Item 1 to 3 is ',shoplist[1:3])
print('Item 2 to end is ',shoplist[2:])
#从正向第一个到反向第一个的区间
print('Item 1 to -1 is ',shoplist[1:-1])
print('Item start to end ',shoplist[:])

#从某一字符串中切片
print('Character 1 to 3 is ',name[1:3])
print('Character 2 to end is ',name[2:])
#从正向第一个到反向第一个的区间
print('Character 1 to -1 is ',name[1:-1])
