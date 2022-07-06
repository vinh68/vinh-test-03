print('Pham mem chuyen doi tien te USD sang VND')
while True:
    USD = input('Nhap so tien theo USD: ')
    if not USD:
        print('Cam on quy khach')
        break
    VND = int(USD)*23500
    print('Gia tri theo tien Viet Nam:', VND, 'vnd')
    print('Ban co muon tiep tuc su dung chuong trinh? Y/N')
    answer=input()
    if answer=='Y':
        pass
    else:
        print('Cam on quy khach')
        break
