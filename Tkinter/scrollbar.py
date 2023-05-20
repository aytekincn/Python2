# "Scrollbar" veya kaydırma çubuğu tek başına kulanılmaz ya metin ya da görsel ile kullanılması lazım.
from tkinter import *

pencere = Tk()

kaydirma = Scrollbar( pencere, orient = HORIZONTAL ) # Bu şekilde  scrollbarı oluştururuz. Horizontal  yazımız yatay bir şekilde oluşturmak istediğimizi gösterir.
kaydirma.pack( side = BOTTOM, fill = X ) # scrollbarın hangi alana dayalı ve hangi axis üzeinde hareket etmesi gerektiğini yazarız.

metin = Text(wrap = NONE ,xscrollcommand = kaydirma.set, width = 30 ) # Burada da textimizle birlikte kullandığımızı belirtiriz. # X ekseninde oluşturmak için alt satıra geçme özelliğini iptal etmeliyiz.
metin.pack()

kaydirma.config( command = metin.xview ) # Kaydırma çubuğunu aktif hale getirmek için kullandığımız fonksiyon.


mainloop()