
# This Python program encrypts and decrypts plaintext by Kalmux.

from tkinter import *

# Functions

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption():

    key = int(key_value.get())
    plain_text = ptext_value.get("1.0", "end-1c").lower()
    cipher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + key) % 26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char 
    
    ctext_value.delete("1.0", "end-1c")
    ctext_value.insert("1.0", cipher_text)


def decryption():
    
    key = int(key_value.get())
    cipher_text = ctext_value.get("1.0", "end-1c").lower()
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - key) % 26
            plain_text += alphabets[new_position]
        else:
            plain_text += char 
    
    ptext_value.delete("1.0", "end-1c")
    ptext_value.insert("1.0", plain_text)


base = Tk()

base.geometry("650x450")
base.maxsize(width=650,height=450)
base.minsize(width=650,height=450)

base.title("Muxcipher")

head_frame = Frame(base)
head_frame.pack()

head_lable = Label(head_frame,text="Welcome To MuxCipher",font=("Times New Roman", 30 ,"bold"),pady=15)
head_lable.pack()

option_frame = Frame(base,pady=10,padx=8)
option_frame.pack(side=TOP,anchor="center")



key_lable = Label(option_frame,text="Shift Key",font=("Times New Roman", 12))
key_lable.grid(row=0,column=4)

key_value = IntVar()
key_value.set(0)
key_value = Entry(option_frame,textvariable=key_value,width=10,font=("Times New Roman", 12))
key_value.grid(row=0,column=5,padx=5)


msg_frame = Frame(base,borderwidth=2,relief=RAISED,width=30)
msg_frame.pack(side=TOP,anchor="nw",padx=20,pady=10)

ptext_lable = Label(msg_frame,text="Plain Text",font=("Times New Roman", 11))
ptext_lable.grid(row=0,column=0,padx=20)

space_lable = Label(msg_frame,text="",padx=190)
space_lable.grid(row=0,column=2)

ctext_lable = Label(msg_frame,text="Cipher Text",font=("Times New Roman", 11))
ctext_lable.grid(row=0,column=3,padx=20)

msgbox_frame = Frame(base,height=80,padx=15)
msgbox_frame.pack(side=TOP,anchor="nw")

ptext_value = Text(msgbox_frame,width=37,height=12,font=("Times New Roman", 12))
ptext_value.grid(row=0,column=0,padx=5)

ctext_value = Text(msgbox_frame,width=37,height=12,font=("Times New Roman", 12))
ctext_value.grid(row=0,column=1,padx=5)

encrypt_button = Button(option_frame,text="Encrypt",command=encryption,font=("Times New Roman", 12),padx=50)
encrypt_button.grid(row=0,column=0,padx=30)

decrypt_button = Button(option_frame,text="Decrypt",command=decryption,font=("Times New Roman", 12),padx=50)
decrypt_button.grid(row=0,column=7,padx=30)

foot_lable = Label(base,text="Created By Kalmux",font=("Courier", 10))
foot_lable.pack(side=TOP,anchor="center",pady=10)

base.mainloop()