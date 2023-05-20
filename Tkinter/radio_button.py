# "radiobutton" pencere aracı, programımızda kullanıcıya tek seçim yaptırmak için kullandığımız pencere aracıdır. Checkbuttondan farkı tek bir seçim yapılabilmesi.

from tkinter import *

pencere = Tk()

baslik = pencere.title("RadioButton")
pencere.geometry("400x400")

var = IntVar() # Sayısal alan fonksiyonunu kullanıyoruz.

soru = Label( text = "Öğrenim Durumunuz Nedir?") # Kullanıcıya sorumuz
soru.pack( anchor = "w")

r1 = Radiobutton( pencere, text = "İlkokul", variable = var, value = 1 ) # RadioButtonun nereye bağlı olacağını yazarız. Sayısal alan fonksiyonuna nereden değer alacaksa  orayı yazarız.
# value = 1 kısmı değer alacağını belirtir.
r1.pack(anchor = "w")

r2 = Radiobutton( pencere, text = "Ortaokul", variable = var, value = 2 ) 
r2.pack(anchor = "w")

r3 = Radiobutton( pencere, text = "Lise", variable = var, value = 3 ) 
r3.pack(anchor = "w")

r4 = Radiobutton( pencere, text = "Lisans", variable = var, value = 4 ) 
r4.pack(anchor = "w")
# Anketler gibi alanlarda kullanılır yan yana side kullanarak yazılır.
mainloop()

























