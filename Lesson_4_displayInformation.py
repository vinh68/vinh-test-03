class Hocvien:
    def __init__(self, hoten=0, ngaysinh=0, diachi=0, background=0, mucdichhocpython=0):
        self.hoten=hoten
        self.ngaysinh=ngaysinh
        self.diachi=diachi
        self.background=background
        self.mucdichhocpython=mucdichhocpython
    def thongtin(self):    
        print('Thong tin cua hoc vien:\n',self.hoten,'\n',self.ngaysinh,'\n',self.diachi,'\n',self.background,'\n',self.mucdichhocpython)
Vinhpro=Hocvien('Nguyen Van Vinhpro','14-01-1995','Hai Duong','Dai hoc y Ha Noi','Hoc de chuyen nganh tim cong viec dung voi so thich. Cac anh chi giup do chung em nhe ^^')
Vinhpro.thongtin()
