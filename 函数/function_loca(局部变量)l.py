# x 是我们这一函数的局部变量。因此，当我们改变函数中
# x 的值的时候，主代码块中的 x 则不会受到影响
x=5
def fun(x):
     print ('x is ',x)
     x=2
     print('Change local x to ',x)

 fun(x)
 print('x is still ',x)
