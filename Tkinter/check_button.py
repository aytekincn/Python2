# CheckButton  Pencere Aracı ( onay kutusu ) bir veya biren fazla seçenek bir araa tercih eilmesi gerektiğine kullanılır.
from tkinter import *
pencere  = Tk()
pencere.geometry("500x400+500+200")
baslik = pencere.title("Sporlar")

soru = Label( text = "Hangi Spor Dallarını Seviyorsunuz?", font = "Arial 12 bold ", bg = "pink" )
soru.grid( row = 0, column = 0) 

futbol = Checkbutton( text = "Futbol")
futbol.place( relx = 0.0, rely = 0.1 )

voleybol = Checkbutton( text = "Voleybol")
voleybol.place( relx = 0.0, rely = 0.2 ) 

basketbol = Checkbutton( text = "Basketbol")
basketbol.place( relx = 0.0, rely = 0.3 )    

tenis = Checkbutton( text = "Tenis")
tenis.place( relx = 0.0, rely = 0.4 )

yüzme = Checkbutton( text = "Yüzme")
yüzme.place( relx = 0.0, rely = 0.5 )

mainloop()
























