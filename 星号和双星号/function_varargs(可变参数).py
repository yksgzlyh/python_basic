def somefunc(a, b, c, *starone, **startwo):
    print (a, b, c)
    print (starone)
    print (startwo)
somefunc(1, 2, 3, 4, 5, 6, arg0=80, arg1=201)
