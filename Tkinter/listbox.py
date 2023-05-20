# "listbox" aracı programımızda seçilebilir bir liste oluşturmamızı sağlayan pencere aracı ( widgets )' dır.
from tkinter import *

pencere = Tk()

baslik = pencere.title("Listbox")
pencere.geometry("400x300")

programlama_dilleri = ["Python","Java","JavaScript","Kotlin","Swift"] # Listbox içerisine sırasıyla koymak istediğimiz elemanlar.

liste = Listbox( bg = "lightgrey", font = "System 12")

for i in programlama_dilleri: # Bu şekilde for döngüsü kullanarak listbox içerisine listemizi daha kolay bir şekilde atayabiliriz.
    liste.insert(END,i)

liste.pack()
mainloop()

# liste.insert(1, "Python") bu şekilde teker teker index numarası ve elemanı yazarak da listbox oluşturulabilir.























