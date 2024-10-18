import tkinter as tk
from tkinter import messagebox
import pyttsx3

def create_window(root):
    # Membuat layout dengan label dan tombol
    label = tk.Label(root, text="Ada Perlu kemana?", font=("Arial", 14))
    label.pack(pady=10)

    btn_cs = tk.Button(root, text="Customer Service", width=20, command=lambda: antrian("Customer Service"))
    btn_cs.pack(pady=5)

    btn_teller = tk.Button(root, text="Teller", width=20, command=lambda: antrian("Teller"))
    btn_teller.pack(pady=5)

    return root

def baca_antrian(nama_file):
    try: 
        with open(nama_file, "r") as file:
            nilai = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        nilai = []
    return nilai

def tulis_antrian(nama_file, antrian):
    with open(nama_file, "a") as file:
        file.write(str(antrian[-1]) + "\n")  # Menulis nilai terakhir dari antrian

def antrian(jenis):
    if jenis == "Customer Service":
        nilai_sebelumnya = baca_antrian("antrian.txt")
        if nilai_sebelumnya:
            antrike = nilai_sebelumnya[-1] + 1
        else:
            antrike = 1
        antri.append(antrike)
        tulis_antrian("antrian.txt", antri)
        messagebox.showinfo("Antrian", f"Anda mendapatkan antrian ke - {antrike}")
    elif jenis == "Teller":
        nilai_teller = baca_antrian("antrianteller.txt")
        if nilai_teller:
            antrike = nilai_teller[-1] + 1
        else:
            antrike = 1
        antri.append(antrike)
        tulis_antrian("antrianteller.txt", antri)
        messagebox.showinfo("Antrian", f"Anda mendapatkan antrian ke - {antrike}")

if __name__ == "__main__":
    antri = []
    engine = pyttsx3.init()
    bahasa = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_idID_Andika"  
    engine.setProperty('voice', bahasa)
    engine.say("Selamat datang di BANK PARIS")
    engine.runAndWait()

    root = tk.Tk()
    root.title("BANK PARIS")
    root.geometry("300x200")

    create_window(root)
    
    engine.say("Silahkan pilih tujuan Anda")
    engine.runAndWait()

    root.mainloop()

    engine.say("Terimakasih! silahkan tunggu")
    engine.runAndWait()
