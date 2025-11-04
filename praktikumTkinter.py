import tkinter as tk
import tkinter.messagebox as msg

top = tk.Tk()
top.title("Aplikasi Prediksi")
top.geometry("350x450")
top.configure(bg="#EBA206")

for i in range(10):
    nilai = tk.Frame()
    nilai.pack(pady=2, padx=10)

    L1 = tk.Label(nilai, text=f"Nilai {i+1}: ", width=10)
    L1.pack(side=tk.LEFT)

    E1 = tk.Entry(nilai, bd=5)
    E1.pack(side=tk.LEFT, fill="x", expand=True)

tombolHasil = tk.Button(top, text="Hasil Prediksi", bg="#FFFFFF")
tombolHasil.pack(pady=20)

luaran = tk.Label(top, text="Luaran hasil prediksi")
luaran.pack(side=tk.BOTTOM)

top.mainloop()