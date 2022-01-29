from tkinter import *

word_list = []
fhand = open("dict.txt")
for line in fhand:
    word_list.append(line.rstrip())

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z"]


def solve(txt_input, start_num=0):
    txt_input = txt_input.lower()
    input_words = txt_input.split()
    try:
        word_input = input_words[start_num]
    except:
        failure.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
        return
    match_list = get_shift(word_input)
    if len(match_list) == 1:
        good_shift = match_list[0]
        failure.grid_forget()
        shift_entry.delete(0, END)
        shift_entry.insert(0, good_shift)
        txt_entry.delete(0, END)
        txt_entry.insert(0, decrypt(txt_input, good_shift))
    if len(match_list) == 0:
        solve(txt_input, start_num=start_num + 1)
    if len(match_list) > 1:
        solve(txt_input, start_num=start_num+1)


def get_shift(word):
    match_list = []
    for shift in range(26):
        plaintext = ''
        for char in word:
            if char not in letters:
                plaintext += char
                continue
            pos = letters.index(char)
            pos -= shift
            if pos > 25 or pos < 0:
                pos = pos % 26
            plaintext += letters[pos]
        if plaintext in word_list:
            match_list.append(shift)
    return match_list


def decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char not in letters:
            plaintext += char
            continue
        pos = letters.index(char)
        pos -= shift
        if pos > 25 or pos < 0:
            pos = pos % 26
        plaintext += letters[pos]
    return plaintext

root = Tk()
root.title("Ceaser Shift Codebreaker")

txt_label = Label(root, text="Plaintext")
txt_label.grid(row=0, column=2, sticky=W, padx=10, pady=(10, 0))
txt_entry = Entry(root)
txt_entry.grid(row=1, column=2, padx=10)
ciphertxt_label = Label(root, text="Ciphertext")
ciphertxt_label.grid(row=0, column=0, sticky=W, padx=10, pady=(10, 0))
ciphertxt_entry = Entry(root)
ciphertxt_entry.grid(row=1, column=0, padx=10)
shift_label = Label(root, text="Shift")
shift_label.grid(row=0, column=1, pady=(10, 0), sticky=W)
shift_entry = Entry(root, width=3)
shift_entry.grid(row=1, column=1)
decrypt_btn = Button(root, text="Decrypt", command=lambda: solve(ciphertxt_entry.get()))
decrypt_btn.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
failure = Label(root, text="Shift could not be determined", fg="red")

root.mainloop()


