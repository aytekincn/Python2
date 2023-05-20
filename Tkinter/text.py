# "text" pencere aracı birden fazla satır içeren metinler yazmamıza yardımcı olur. Bir widgetsdır.

from tkinter import *

pencere = Tk()

pencere.geometry("500x400+500+200")
baslik = pencere.title("Veri Kaydetme Programı")

def kaydet():
    kayit= veri.get( 1.0, END ) # Texten hangi veriyi alacağını belirtiriz. Satırlar 1' den sütunlar 0' dan başlar.
    dosya = dosya.open("kayit.txt", "w")
    dosya.write( kayit )



veri = Text( bg = "lightgrey", font = "Arial 15 italic")
veri.pack()

dugme = Button( text = "Dosyaya Kaydet", command = kaydet )
dugme.pack()






mainloop()





















