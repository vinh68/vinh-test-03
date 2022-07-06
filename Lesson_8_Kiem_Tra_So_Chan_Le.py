print('Chuong trinh kiem tra so chan le')
print('Codygym')
number=input('Moi ban nhap so:')
while True:
    if number.isnumeric() :
        number=int(number)
        print('So hop le')
        if number%2==0:
            print(number,'la so chan !')
        else:
            print(number,'la so le !')
        print('Quy khach co muon tiep tuc ? Y/N')
        answer=input()
        if answer=='Y':
            continue
        else:
            print('Cam on quy khach')
            break
    else:
        print('Moi quy khach nhap lai')
