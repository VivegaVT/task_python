import tkinter as tk

def hitung_diskon():
    harga = float(input_harga.get())
    diskon = float(input_diskon.get())
    hasil = harga * (1 - (diskon / 100))

    label_hasil.config(text=f"Final Price: Rp. {hasil:.2f}")


jendela = tk.Tk()
jendela.title("Discount Calculator")
jendela.geometry("250x250")

tk.Label(jendela, text="Original Price:").pack()
input_harga = tk.Entry(jendela)
input_harga.pack()

tk.Label(jendela, text="Discount (%):").pack()
input_diskon = tk.Entry(jendela)
input_diskon.pack()

tombol = tk.Button(jendela, text="Calculate", command=hitung_diskon)
tombol.pack()

label_hasil = tk.Label(jendela, text="Final Price: Rp. ,00")
label_hasil.pack()

jendela.mainloop()