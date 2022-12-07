# Nama Program      : Aplikasi Vigenere & Triangle Cipher
# Nama Anggota 1    : Rheza Pandya Andhikaputra (140810200023)
# Nama Anggota 2    : Andyka Baswara Putra (140810200061)
# Nama Anggota 3    : Muhammad Ariiq Rakha Shafa (140810200064)
# Kelas             : A
# Tugas             : Tugas Akhir Project Praktikum Kriptografi

# untuk button & GUI
from tkinter import *
from random import *
import tkinter as tk
import numpy as np # untuk kalkulasi

# membuat window object
window = Tk()

# ukuran window
window.geometry("800x600")

# judul window
window.title("Project UAS : Vigenere & Triangle Cipher")

# background window
window.configure(bg = 'white')

# inisialisasi
rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# fungsi exit
def qExit():
    window.destroy()

# fungsi reset
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")

# entry
entry_the_text = Entry(window, width = 40, textvariable = Msg)
entry_the_text.place(x = 350, y = 120)

entry_key = Entry(window, width = 40, textvariable = key)
entry_key.place(x = 350, y = 160)

entry_ED = Entry(window, width = 40, textvariable = mode)
entry_ED.place(x = 350, y = 200)

entry_the_converted_text = Entry(window, width = 40, textvariable = Result)
entry_the_converted_text.place(x = 350, y = 360)

# label
Label(window,text= 'Aplikasi Vigenere & Triangle Cipher', bg = 'white', fg = 'black', font=('helvetica', 25)).place(x = 120, y = 30)
Label(window, text = 'Message:', bg = 'white',  fg = 'black', font=('helvetica', 15)).place(x = 50, y = 120)
Label(window, text = 'Key:' , bg = 'white',  fg = 'black', font = ('helvetica', 15)).place(x = 50, y = 160)
Label(window, text = 'e for Encrypt / d for Decrypt' , bg = 'white',  fg = 'black', font=('helvetica', 15)).place(x = 50, y = 200)
Label(window, text = 'Result Message:' , bg = 'white',  fg = 'black', font = ('helvetica', 15)).place(x = 50, y = 360)
Label(window, text = 'Team : ' , bg = 'white',  fg = 'black', font = ('helvetica', 14)).place(x = 50, y = 400)
Label(window, text = 'Rheza Pandya - 140810200023 ' , bg = 'white',  fg = 'black', font = ('helvetica', 12)).place(x = 50, y = 440)
Label(window, text = 'Andyka Baswara - 140810200061 ' , bg = 'white',  fg = 'black', font = ('helvetica', 12)).place(x = 50, y = 470)
Label(window, text = 'M. Ariq Rakha - 140810200064 ' , bg = 'white',  fg = 'black', font = ('helvetica', 12)).place(x = 50, y = 500)

# Fungsi enkripsi vigenere cipher
def enkripsi_vigenere(key, clear):
    if key == "":
        key = "a"
    enc_text = ""	

    if len(key) > len(clear):
        key = key[: len(clear)]
    elif len(key) < len(clear):
        key += clear
        key = key[:len(clear)]
        key += clear[:len(key)]

    for i in range(len(clear)):
        if clear[i].isupper(): 
            v = 'A'
        elif clear[i].islower(): 
            v = 'a'
        else:
            enc_text += clear[i]
            continue

        enc_text += (chr(((ord(clear[i]) - 2 * ord(v) + ord(key[i])) % 26) + ord(v)))
    return enc_text

# Fungsi dekripsi vigenere cipher
def dekripsi_vigenere(key, clear):
    if key == "":
        key = "a"
    dec_text = ""

    for i in range(len(clear)):
        if clear[i].isupper(): 
            v = 'A'
        elif clear[i].islower(): 
            v = 'a'
        else:
            dec_text += clear[i]
            continue

        s = ord(clear[i]) - ord(key[i])
        if s < 0: 
            s += 26
        v_k = chr(s + ord(v))
        key += v_k
        dec_text += v_k
    return dec_text


# Fungsi enkripsi triangle cipher
def enkripsi_triangle(k, clear):
    row = 0
    min = 1
    huruf = []
    plaintext = clear
    panjang = len(plaintext)
    while (panjang > 0):
        panjang -= min
        huruf.append(min)
        min += 2
        row += 1
    col = min - 2

    for i in range (panjang, 0):
        plaintext += "x"
    segitiga = np.full((row, col), None)

    count = 0
    for i in range(row):
        tempcol = int(((col-1)/2)-i)
        for j in range(huruf[i]):
            segitiga[i][tempcol] = plaintext[count]
            count += 1
            tempcol +=1

    enc = ""
    for i in range(col):
        for j in range(row):
            if segitiga[j][i] == None:
                continue
            else:
                enc += segitiga[j][i]
    return enc


# Fungsi dekripsi triangle cipher
def dekripsi_triangle(clear):
    row = 0
    min = 1
    huruf = []
    panjang = len(clear)
    while (panjang > 0):
        panjang -= min
        huruf.append(min)
        min += 2
        row += 1
    col = min - 2
    segitiga = np.full((row, col), None)

    count = 0
    for i in range(row):
        tempcol = int(((col-1)/2)-i)
        for j in range(huruf[i]):
            segitiga[i][tempcol] = clear[count]
            count += 1
            tempcol +=1

    count = 0
    for i in range(col):
        for j in range(row):
            if segitiga[j][i] == None:
                continue
            else:
                segitiga[j][i] = clear[count]
                count += 1

    dec = ""
    for i in range(row):
        for j in range(col):
            if segitiga[i][j] == None:
                continue
            else:
                dec += segitiga[i][j]

    return dec.replace('x','')

# Fungsi untuk run vigenere cipher
def RunVigenere():
    print("Message= ", (Msg.get()))

    clear = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(enkripsi_vigenere(k, clear))
    elif (m == 'd'):
        Result.set(dekripsi_vigenere(k, clear))

# Fungsi untuk run triangle cipher
def RunTriangle():
    print("Message= ", (Msg.get()))

    clear = Msg.get()
    k = key.get()
    m = mode.get()  

    if (m == 'e'):
        Result.set(enkripsi_triangle(k, clear))
    elif (m == 'd'):
        Result.set(dekripsi_triangle(clear))

# Tombol-tombol
btn_vigenere  = Button(window, fg = "white",
                        font = ('roboto', 16, 'bold'), width = 10,
                    text = "Run Vigenere", bg = "green", command = RunVigenere).place(x = 50, y = 270 )

btn_triangle  = Button(window, fg = "white",
                        font = ('roboto', 16, 'bold'), width = 10,
                    text = "Run Triangle", bg = "green", command = RunTriangle).place(x = 200, y = 270 )

btn_reset = Button( fg = "white",
                        font = ('roboto', 16, 'bold'), width = 10,
                    text = "Reset", bg = "blue", command = Reset).place(x = 350, y = 270 )

btn_exit = Button( fg = "white",
                        font = ('roboto', 16, 'bold'), width = 10,
                    text = "Exit", bg = "red", command = qExit).place(x = 500, y = 270)

# agar window tetap jalan
window.mainloop()