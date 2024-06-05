import tkinter as tk
from tkinter import messagebox


def toplama(x, y):
    return x + y


def cikarma(x, y):
    return x - y


def carpma(x, y):
    return x * y


def bolme(x, y):
    if y == 0:
        return "Bir sayı 0'a bölünmez"
    return x / y


def hesapla():
    try:
        sayi1 = float(entry1.get())
        sayi2 = float(entry2.get())
        islem = secim.get()

        if islem == "Toplama":
            sonuc = toplama(sayi1, sayi2)
        elif islem == "Çıkarma":
            sonuc = cikarma(sayi1, sayi2)
        elif islem == "Çarpma":
            sonuc = carpma(sayi1, sayi2)
        elif islem == "Bölme":
            sonuc = bolme(sayi1, sayi2)

        sonuc_label.config(text=f"CEVAP: {sonuc}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin")


root = tk.Tk()
root.title("Hesap Makinesi")

secim = tk.StringVar()
secim.set("Toplama")

label1 = tk.Label(root, text="İlk sayıyı girin:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="İkinci sayıyı girin:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root, text="İşlem:")
label3.grid(row=2, column=0)

dropdown = tk.OptionMenu(root, secim, "Toplama", "Çıkarma", "Çarpma", "Bölme")
dropdown.grid(row=2, column=1)

hesapla_button = tk.Button(root, text="Hesapla", command=hesapla)
hesapla_button.grid(row=3, column=0, columnspan=2)

sonuc_label = tk.Label(root, text="CEVAP: ")
sonuc_label.grid(row=4, column=0, columnspan=2)
root.mainloop()
