# This Python tool encrypts and decrypts image, by Kalmux.

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


def filepath():
    global image, photo
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.tiff;*.webp;*.heif")])

    if file_path:

        try:
            image = Image.open(file_path)
            image.thumbnail((200, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            image_display.config(image=photo)
            image_display.image = photo 
            path_value.set(file_path)

        except Exception as e:
            print(f"An error occurred: {e}")


def encrypt():
    pass


def decrypt():
    pass


base = Tk()

base.geometry("600x400")
base.title("ImgCrypt")

head_frame = Frame(base)
head_frame.pack(pady=10)

head_lable = Label(head_frame,text="Welcome to ImgCrypt",font=("Times New Roman", 30 ,"bold"))
head_lable.pack()


file_frame = Frame(base)
file_frame.pack(side=TOP,anchor="nw",pady=5,padx=8)


file_lable = Label(file_frame,text="Image Path:",font=("Times New Roman", 15))
file_lable.grid(row=1,column=0)

path_value = StringVar()
path_value.set("")
path = Entry(file_frame,textvariable=path_value,font=("Times New Roman", 12),width=50)
path.grid(row=1,column=2)

path_button = Button(file_frame,text="Browse",command=filepath,font=("Times New Roman", 11),padx=10)
path_button.grid(row=1,column=3,padx=5)

key_frame = Frame(base)
key_frame.pack(side=TOP,anchor="nw")

space_lable = Label(key_frame,text="",padx=30)
space_lable.grid(row=0,column=0)

key_lable = Label(key_frame,text="Key:",font=("Times New Roman", 14))
key_lable.grid(row=0,column=1)

key_value = IntVar()
key_value = Entry(key_frame,textvariable=key_value,font=("Times New Roman", 12),width=10)
key_value.grid(row=0,column=2)

space_lable = Label(key_frame,text="",padx=57)
space_lable.grid(row=0,column=3)

encrypt_button = Button(key_frame,text="Encrypt",font=("Times New Roman", 11),width=15)
encrypt_button.grid(row=0,column=4,padx=10)
decrypt_button = Button(key_frame,text="Decrypt",font=("Times New Roman", 11),width=15)
decrypt_button.grid(row=0,column=5,padx=5)


image_frame = Frame(base,borderwidth=3,relief=SUNKEN,height=200,width=200)
image_frame.pack(side=TOP,anchor="center",expand=False,pady=15)

image_display = Label(image_frame,height=200,width=200,text="No Image Selected")
image_display.pack(expand=True)

image_frame.pack_propagate(False)


base.mainloop()