# Tkinter biçimlendirme işlemleri.
from tkinter import *

pencere = Tk()

baslik = pencere.title("Biçimlendirme")

etiket = Label(text = "Merhaba", fg = "blue", font = "System 30 underline ") # Burada yazdırdığımız etiketin fontunu ve boyutunu ayarlayabiliriz.
#  Yazı tipinin de şeklini eğik vs değiştirilebilir. italic, bold vb şekillerde biçimlendirilebilir. Birlikte de kullanılabilir bold underline gibi.

etiket2 = Label( text = "Python\nAytekin\tCan", font = " Arial 50 bold underline", # \n kullanılabilir etiket içerisinde veya \t .
                cursor = "pirate") # cursor ( imleç ) değişikliği de yapılabilir cursor list üzerinden ulaşılabilir. Yazdığımız etiket üzerine gelindiğinde cursor değişir.

etiket.pack()
etiket2.pack()

mainloop()

















