import tkinter as tk
from tkinter import messagebox
import pyttsx3
import multiprocessing

def panggil_antrian_cs(slot, engine):
    with open("antrian.txt", "r") as file:
        baca = [line.strip() for line in file.readlines()]
    if baca:
        nk = baca.pop(0)
        messagebox.showinfo("Panggilan Antrian", f"Antrian ke-{nk} menuju customer service {slot}")
        engine.say(f"Antrian ke-{nk}, menuju customer service {slot}")
        engine.runAndWait()
        with open("antrian.txt", "w") as file:
            for antrian in baca:
                file.write(antrian + "\n")
    else:
        messagebox.showinfo("Panggilan Antrian", "Tidak ada antrian tersisa")
        

def create_gui(queue, slot):
    def panggil():
        queue.put("Panggil")

    root = tk.Tk()
    root.title(f"Customer Service {slot}")

    label = tk.Label(root, width=40, text=f"Panggil Antrian Selanjutnya")
    label.pack(pady=20)

    button = tk.Button(root, text="Panggil", command=panggil)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    # Buat pyttsx3 engine di proses utama
    engine = pyttsx3.init()
    bahasa = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_idID_Andika"
    engine.setProperty('voice', bahasa)

    queue1 = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()

    proses1 = multiprocessing.Process(target=create_gui, args=(queue1, "A"))
    proses2 = multiprocessing.Process(target=create_gui, args=(queue2, "B"))

    proses1.start()
    proses2.start()

    while True:
        if not queue1.empty():
            panggil_antrian_cs("A", engine)
            queue1.get()

        if not queue2.empty():
            panggil_antrian_cs("B", engine)
            queue2.get()
            
        if not proses1.is_alive() and not proses2.is_alive():
            break