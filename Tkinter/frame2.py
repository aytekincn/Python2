# 4 tane buton hazırlayıp frame kullanarak hizalayacağız.
from tkinter import *

pencere = Tk()
pencere.geometry("500x500+600+200")
baslik = pencere.title("Frame Buton")

cerceve = Frame( pencere )
cerceve.pack()

cerceve2 = Frame( pencere )
cerceve2.pack( side = BOTTOM )

ac = Button(cerceve, text = "Aç") # Hangi frame' e dahil etmek istersek textten önce o framenin ismini ekleriz.
ac.pack( side = LEFT )

kaydet = Button( cerceve, text = "Kaydet")
kaydet.pack( side = LEFT )

iptal = Button( cerceve2, text = "İptal")
iptal.pack( side = LEFT )

cikis = Button( cerceve2, text = "Çıkış" )
cikis.pack( side = BOTTOM )   

mainloop()





























