from tkinter import *
from random import *
import tkinter as tk

# creating window object
window = Tk()

# defining size of window
window.geometry("800x600")

# setting up the title of window
window.title("Project UAS Vigenere Triangle")

## setting the background color
window.configure(bg = 'white')

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# exit function
def qExit():
    window.destroy()

# Function to reset the window
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


# adding entries
entry_the_text = Entry(window, width = 40, textvariable = Msg)
entry_the_text.place(x = 350, y = 120)

entry_key = Entry(window, width = 40, textvariable = key)
entry_key.place(x = 350, y = 160)

entry_ED = Entry(window, width = 40, textvariable = mode)
entry_ED.place(x = 350, y = 200)

entry_the_converted_text = Entry(window, width = 40, textvariable = Result)
entry_the_converted_text.place(x = 350, y = 360)


# labels
Label(window,text= 'VIGNERE TRIANGLE', bg = 'white', fg = 'black', font=('helvetica', 25)).place(x = 120, y = 30)
Label(window, text = 'Message:', bg = 'white',  fg = 'black', font=('helvetica', 15)).place(x = 50, y = 120)
Label(window, text = 'Key:' , bg = 'white',  fg = 'black', font = ('helvetica', 15)).place(x = 50, y = 160)
Label(window, text = 'e for Encrypt / d for Decrypt' , bg = 'white',  fg = 'black', font=('helvetica', 15)).place(x = 50, y = 200)
Label(window, text = 'Result Message:' , bg = 'white',  fg = 'black', font = ('helvetica', 15)).place(x = 50, y = 360)
Label(window, text = 'Team : ' , bg = 'white',  fg = 'black', font = ('helvetica', 14)).place(x = 50, y = 400)
Label(window, text = 'Rheza Pandya - 140810200023 ' , bg = 'white',  fg = 'black', font = ('helvetica', 12)).place(x = 50, y = 440)
Label(window, text = 'Andyka Baswara - 140810200061 ' , bg = 'white',  fg = 'black', font = ('helvetica', 12)).place(x = 50, y = 470)
Label(window, text = 'M. Ariq Rakha - 140810200064 ' , bg = 'white',  fg = 'black', font = ('helvetica', 12)).place(x = 50, y = 500)

# Vigenere Cipher
import numpy as np
# Function to encode
def encode(key, clear):
    if key == "":
        key = "a"
    enc_text = ""	

    if len(key) > len(clear):
        key = key[: len(clear)]
    elif len(key) < len(clear):
        key += clear
        key = key[:len(clear)]
        # key += clear[:len(key)]
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

# Function to decode
def decode(key, clear):
    clear = decode_triangle(clear)
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


#Function triangle encryption
def encode_triangle(k, clear):
    row = 0
    min = 1
    huruf = []
    plaintext = encode(k,clear)
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


#Function triangle decryption
def decode_triangle(clear):
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
    return dec

def Ref():
    print("Message= ", (Msg.get()))

    clear = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'encrypt' or 'enkripsi'):
        Result.set(encode(k, clear))
    else:
        Result.set(decode(k, clear))

def Ref2():
    print("Message= ", (Msg.get()))

    clear = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'encrypt' or 'enkripsi'):
        Result.set(encode_triangle(k, clear))
    else:
        Result.set(decode(k, clear))
## adding buttons

btn_Vigenere_message  = Button( fg = "white",
                        font = ('roboto', 16, 'bold'), width = 10,
                    text = "Vigenere", bg = "blue", command = Ref).place(x = 50, y = 290 )

btn_Triangle_message  = Button( fg = "white",
                        font = ('roboto', 16, 'bold'), width = 10,
                    text = "Triangle", bg = "blue", command = Ref2).place(x = 250, y = 290 )


btn_reset = Button( fg = "white",
                        font = ('roboto', 16, 'bold'), width = 10,
                    text = "Reset", bg = "blue", command = Reset).place(x = 430, y = 290 )



btn_exit = Button( fg = "white",
                        font = ('roboto', 16, 'bold'), width = 10,
                    text = "Exit", bg = "red", command = qExit).place(x = 600, y = 290)

# keeps window alive
window.mainloop()