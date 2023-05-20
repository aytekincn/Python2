from tkinter import *

pencere = Tk()

baslik = pencere.title("Pencere Boyutlandırma")

pencere.geometry("600x400+200+200") # Penceremizi geometry fonksiyonu ile boyutlandırırız. Yanına ise pencerenin ekranın neresinde açılacağını belirtiriz.

# maxsize ve minsize kullanarak arayüzü nereye kadar büyültüp küçültülebileceğini ayarlayabiliriz.
# pencere.minsize( 200, 150) # tırnak kullanmadan.
# pencere.maxsize( 800, 600 ) # maximum ulaşabilecek boyutu ayarlarız.

pencere.resizable(FALSE, FALSE) # Kullanıcının pencere boyutunu arttırıp azaltmasını engellemek için kullanılır. TRUE veya FALSE değer alır ilk sıradaki enine diğeri ise boyuna için geçerli.

etiket = Label( text = "Merhaba")

etiket.pack()



mainloop()












