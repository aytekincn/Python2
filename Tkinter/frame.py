# frame aracılığıyla penceremize çerçeveler ekleyebiliyoruz. Eklenen pencerelerle içerisindeki  öğeleri daha rahat konumlayabilir.
from tkinter import *

pencere = Tk()
pencere.geometry("500x500+600+200")
baslik = pencere.title("Frame oluşturma")

etiket = Label( text = "Adınızı Giriniz :") 
etiket.pack()
# Bu şekilde ayarlandığında aralarında mesafe olmadan alt alta sıralanır ancak frame kullanarak bunu değiştirebiliriz.

cerceve2 = Frame()
cerceve2.pack( pady = 3 )

giris = Entry()
giris.pack()

cerceve = Frame() # Bu şekilde entryden sonra çerçeve yapmak istediğimiz için entryden sonra butondan önce yazarız.
cerceve.pack( pady = 5 ) # Axis belirtiriz hangi düzlem üzerinden yapacağımızı padx veya pady. Burada eklediğimiz sayı arasında o kadar mesafe bırakır.

dugme = Button( text = "Kaydet")
dugme.pack()

mainloop()

















