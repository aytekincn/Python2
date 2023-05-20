from tkinter import *

pencere = Tk()

baslik = pencere.title("Buton Oluşturmak")
pencere.geometry("400x400")


def giris():
    baslik2 = pencere.title("Giriş")
    etiket = Label( text = "Hoşgeldiniz")
    etiket.pack()
    mainloop()

dugme1 = Button( text = "Giriş",  fg = "blue", command = giris)
dugme1.pack()

dugme2 = Button( text = "Çıkış", width = 6, height = 3, fg = "blue", command = pencere.quit ) # Buton oluşturmak için kullandığımız fonksiyon. fg ve bg kullanarak buton rengi değiştirilebilir.
# command fonksiyonu ile butona komut verebiliriz quit vb .

dugme2.pack( side = TOP ) # Düğmeyi de yazıda olduğu gibi pencerenin içinde görünmesi için pack fonksiyonu ile atarız. # side fonksiyonu ile butonun sağ sol üst veya alt kısma dayanacağını ayarlayabiliriz.



mainloop()


























