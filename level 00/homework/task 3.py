def func(list1):
    a = list1[0]
    b = list1[1]
    c = list1[2]
    d = list1[3]
    e = list1[4]
    if a > b and a > c and a > d and a > e:
        return a
    elif b > a and b > c and b > d and b > e:
        return b
    elif c > a and c > b and c > d and c > e:
        return c
    elif d > a and d > b and d > c and d > e:
        return d
    elif e > a and e > b and e > c and e > d:
        return e
    else:
        return "2 numbers are equal to each other and they are max ones"
    
print (func([1, 2, 3, 4, 5]))