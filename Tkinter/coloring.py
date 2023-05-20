# metin renklendirme için 2 tane yapı kullanıyoruz. 
# fg Pencere içerisine yazdığımız metne renk vermek için kullanılır.
# bg Pencere içerisine yazdığımız metnin zeminine renk vermek için kullanılır.

from tkinter import *

pencere = Tk()

baslik = pencere.title("Aytekin Can Tkinter Coloring")

etiket = Label( text = "Bu yazı renklenecek ", fg = "red", bg = "black") # Yazdığımız renkler yerine Html color charttan renklerin kodlarını yazarak da ekleyebiliriz.

etiket.pack()

mainloop()



































