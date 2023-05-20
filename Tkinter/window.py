from tkinter import * # Tkinter ile ilgili bütün içerikleri almak için import * yapıyoruz.

pencere = Tk()   # Tk objesi oluşturuyoruz pencere değişkeninin içine.

baslik = pencere.title("Aytekin Can Tkinter ") # Arayüzümüze başlık oluşturmak için kullandığımız fonksiyon.

etiket = Label( text = "Tkinter Arayüz") # Arayüz içine yazdığımız etiket için kullanılan fonksiyon.
etiket.pack() # Etiketin arayüzde gözükmesi için pack fonksiyonunu kullanıyoruz.

mainloop()


