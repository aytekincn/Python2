# Entry pencere aracı ile kullanıcının metin girebileceği tek satırlık bir alan oluştururuz.
# Diğer pencere araçlarında olduğu gibi isim tanımlayıp paketleme işlemi gerçekleştiririz.

from tkinter import *

pencere = Tk()
pencere.geometry("400x400")

def sil():
    veri.delete( 0, END ) # Kullanıcının girdiği bütün değerleri silmek için END yapısını kullanıyoruz.

veri = Entry()
veri.pack()

dugme1 = Button( text = "Sil",width =30, comman = sil )
dugme1.pack()

dugme2 = Button( text = "Çıkış",width = 30, command = pencere.quit )
dugme2.pack()




mainloop()



















