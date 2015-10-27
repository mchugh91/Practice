__author__ = 'Ciaran'
def manyRangeTests ():
    range1 = range (10)
    range2 = range (1 ,10)
    range3 = range (0 ,10)
    range4 = range (10 ,-10, )
    print ('--- range1 ---')
    for counter in range1 :
        print ( counter )
    print ('--- range2 ---')
    for counter in range2 :
        print ( counter )
    print ('--- range3 ---')
    for counter in range3 :
        print ( counter )
    print ('--- range4 ---')
    for counter in range4 :
        print ( counter )

manyRangeTests ()