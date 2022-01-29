from tkinter import *


def Ceaser_Shift(E_Not_D):
    if E_Not_D:
        plaintext = txt_entry.get()
        shift = int(shift_entry.get())
    else:
        plaintext = ciphertxt_entry.get()
        shift = 0-int(shift_entry.get())
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
               "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y", "z"]
    ciphertext = ""
    for char in plaintext.lower():
        if char not in letters:
            ciphertext += char
            continue
        pos = letters.index(char)
        pos += shift
        if pos > 25 or pos < 0:
            pos = pos % 26
        ciphertext += letters[pos]
    if E_Not_D:
        ciphertxt_entry.delete(0, END)
        ciphertxt_entry.insert(0, ciphertext)
    else:
        txt_entry.delete(0, END)
        txt_entry.insert(0, ciphertext)



root = Tk()
root.title("Ceaser Shift")

txt_label = Label(root, text="Plaintext")
txt_label.grid(row=0, column=0, sticky=W, padx=10, pady=(10, 0))
txt_entry = Entry(root)
txt_entry.grid(row=1, column=0, padx=10)
ciphertxt_label = Label(root, text="Ciphertext")
ciphertxt_label.grid(row=0, column=1, sticky=W, padx=10, pady=(10, 0))
ciphertxt_entry = Entry(root)
ciphertxt_entry.grid(row=1, column=1, padx=10)
shift_label = Label(root, text="Shift")
shift_label.grid(row=2, column=0, sticky=E, pady=(10, 0), padx=10)
shift_entry = Entry(root, width=3)
shift_entry.grid(row=3, column=0, sticky=E, pady=(0, 10))
encrypt_btn = Button(root, text="Encrypt", command=lambda: Ceaser_Shift(True))
encrypt_btn.grid(row=2, column=1, sticky=W, padx=10)
decrypt_btn = Button(root, text="Decrypt", command=lambda: Ceaser_Shift(False))
decrypt_btn.grid(row=3, column=1, sticky=W, padx=10)

root.mainloop()
