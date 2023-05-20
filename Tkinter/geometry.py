# Geometry yöneticileri pack() gibi.

from tkinter import *

pencere = Tk()
pencere.geometry("500x400+500+200")

"""
baslik = pencere.title("Geometri Yöneticileri")

yesil_serit = Label( text = "Yeşil Şerit", fg = "green", bg = "lightgreen", font = "Arial 15 bold ")
yesil_serit.pack( expand = YES, fill = BOTH ) # Buradaki expand orantılı bir şekilde labelleri dağıtır

mavi_serit = Label( text = "Mavi Şerit", fg = "blue", bg = "lightblue", font = "Arial 15 bold ")
mavi_serit.pack( expand = YES, fill = BOTH ) # Fill komutu eksene göre etiketleri doldurur. x ekseni yatay Y ekseni dikey BOTH olursa iki taraflı da

kirmizi_serit = Label( text = "Kırmızı Şerit", fg = "red", bg = "pink", font = "Arial 15 bold ")
kirmizi_serit.pack( expand = YES, fill = BOTH ) # side komutunu kullanarak bir kısma doğru yaslayabiliriz.
"""
"""
baslik = pencere.title("Geometri Yöneticileri")

yesil_serit = Label( text = "Yeşil Şerit", fg = "green", bg = "lightgreen", font = "Arial 15 bold ")
yesil_serit.grid( row = 0, column = 0) # Grid komutu labellerimizi hangi satır ve sütuna koyacağımızı sağlar soldan başlar sağa doğru.

mavi_serit = Label( text = "Mavi Şerit", fg = "blue", bg = "lightblue", font = "Arial 15 bold ")
mavi_serit.grid( row = 1, column = 0 )

kirmizi_serit = Label( text = "Kırmızı Şerit", fg = "red", bg = "pink", font = "Arial 15 bold ")
kirmizi_serit.grid( row = 2, column = 0 )
"""
baslik = pencere.title("Geometri Yöneticileri")

yesil_serit = Label( text = "Yeşil Şerit", fg = "green", bg = "lightgreen", font = "Arial 15 bold ")
yesil_serit.place( relx = 0.1, rely = 0.1) # Grid komutu labellerimizi hangi satır ve sütuna koyacağımızı sağlar soldan başlar sağa doğru.

mavi_serit = Label( text = "Mavi Şerit", fg = "blue", bg = "lightblue", font = "Arial 15 bold ")
mavi_serit.place( relx = 0.2, rely = 0.2 )

kirmizi_serit = Label( text = "Kırmızı Şerit", fg = "red", bg = "pink", font = "Arial 15 bold ")
kirmizi_serit.place( relx = 0.3, rely = 0.3 )
# Buradaki place komutu daha ince ayarlarla yerini belirtmemizi sağlar.



mainloop()

























