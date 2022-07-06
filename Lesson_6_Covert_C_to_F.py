print('Chuong trinh chuyen doi do C sang do F')
result=0
while True:
    degreeC=input('Xin moi nhap do C: ')
    if not degreeC:
        print('Cam on ban da su dung chuong trinh')
        break
    degreeF = int((degreeC))*1.8+32
    print('Ket qua:',degreeC ,'^C = ', degreeF,'^F',sep='')
print('\n')