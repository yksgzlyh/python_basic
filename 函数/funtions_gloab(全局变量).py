x=50
def fun():
    global x
    print('x is ',x)
    x=60
    print('The x is change to ',x)
fun()
print('The value of x is ',x)
