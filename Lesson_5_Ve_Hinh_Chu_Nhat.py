# Ve hinh chu nhat
c=input('Nhap ky tu: ')
w=int(input('Nhap chieu dai hinh chu nhat: '))
h=int(input('Nhap chieu rong hinh chu nhat: '))

for i in range(w):
	for j in range(h):
		if i==0 or i==w-1 or j==0 or j==h-1:
			print('*',end=' ')
		else:
			print(' ',end=' ')
		
	print()