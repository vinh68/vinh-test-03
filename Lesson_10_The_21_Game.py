# Game Sum of 21
while True:
    import random as r
    s=0 # Tổng điểm cộng dồn
    # n=0: người chơi được chơi trước
    # n=1: máy tính được chơi trước
    n=r.randint(0,1)
    if n==0:
        print('Bạn được chơi trước')
    else:
        print('Máy tính được chơi trước')

    while s<21:
        if n==1:
            x=r.randint(1,3)
            print('Máy tính đã nhập số:',x)
            s=s+x
            print('Tổng điểm hiện tại: ',s)
            if s>=21:
                print('Bạn đã chiến thắng')
                break
            while True:
                y=int(input('Mời bạn nhập số (1-3): '))
                if y==1 or y==2 or y==3 :
                    break
            # y=int(input('Mời bạn nhập số (1-3): '))
            s=s+y
            if s>=21:
                print('Bạn đã thua')
                break
            print('Tổng điểm hiện tại: ',s)
        else:
            while True:
                y=int(input('Mời bạn nhập số (1-3): '))
                if y==1 or y==2 or y==3 :
                    break
            # y=int(input('Mời bạn nhập số (1-3): '))
            s=s+y
            if s>=21:
                print('Bạn đã thua')
                break
            print('Tổng điểm hiện tại: ',s)
            x=r.randint(1,3)
            print('Máy tính đã nhập số:',x)
            s=s+x
            print('Tổng điểm hiện tại: ',s)
            if s>=21:
                print('Bạn đã chiến thắng')
                break
    
    print('Kết thúc cuộc chơi')
    answer=input('Bạn có muốn tiếp tục chơi ? Y/N')
    if answer=='Y':
        print('Chương trình sẽ được tiếp tục trong giây lát')
    else:
        print('Chương trình đã kết thúc')
        break
