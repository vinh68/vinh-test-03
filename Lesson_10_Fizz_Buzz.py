# Game Fizz Buzz

a=input('Nhap so bat dau: ')
b=input('Nhap so ket thuc: ')
if a.isnumeric() and b.isnumeric() and(b>a):
    list=[x for x in range(int(a),int(b)+1)]
    for n in list:
        if n%3!=0 and n%5!=0:
            print(n,end=', ')
        elif n%3==0 and n%5!=0:
            print('Fizz',end=' ')
        elif n%3!=0 and n%5==0:
            print('Buzz',end=' ')
        elif n%3==0 and n%5==0:
            print('Fizz Buzz',end=' ')
else:
    print('So khong hop le')
