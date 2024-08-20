# This python tool will check your password strength 
# By kalmux

import re
from tkinter import *

path = r"10-million-password-list-top-1000000.txt" # If any error occurs, Change This Path According To Your File System.

def passleak(password):
    global leakscore
    leakscore = 0
    with open (path, 'r') as f:
        passwords = f.read().splitlines()

    if password in passwords:
        return True
    leakscore += 1
    return False


def lengthcheck(password):
    score = 0
    length = len(password)
    if length < 8:
        score = 0
    if length >= 8:
        score += 1
    if length > 12:
        score += 1
    if length > 16:
        score += 1
    if length > 20:
        score += 1

    return score

def charcheck(password):
    score = 0
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1
    
    if has_special:
        score += 1
    

    return score

def repetition(password):
    # Regex to find any character repeated more than two times consecutively
    pattern = r'(.)\1{2,}'
    match = re.search(pattern, password)
    
    if match:
        status_lable.config(text=f"Consecutive character repetition found: {match.group()}",fg="red")
        return 0
    return 1 
    



def main():
    password = passwordvar.get()
    if password == "" :
        status_lable.config(text="No Password Entered",fg="red")
        return
    if lengthcheck(password) == 0:
        status_lable.config(text="Password Length is too short !",fg="red")
        return
    if  repetition(password) == 0:
        return
    if not passleak(password):
        length_score = lengthcheck(password)
        char_score = charcheck(password)
        repetition_score = repetition(password)
        total_score = length_score + char_score + leakscore + repetition_score
        

        if total_score <= 3:
            status_lable.config(text="Very Weak",fg="red")
        elif total_score > 3 and total_score <= 5:
            status_lable.config(text="Weak",fg="orange")
        elif total_score > 5 and total_score <= 7:
            status_lable.config(text="Moderate",fg="yellow")
        elif total_score > 7:
            status_lable.config(text="Strong",fg="green")
    else:
        status_lable.config(text="Password found in data leak !",fg="red")
        


base = Tk()
base.geometry("450x250")
base.maxsize(width=450,height=250)
base.minsize(width=450,height=250)
base.title("Passify")
base.config(bg="#1C1C1C")

head_frame = Frame(base,bg="#1C1C1C")
head_frame.pack(side=TOP,anchor="center",pady=10)

head_lable = Label(head_frame,text="Welcome To Passify",font=("Times New Roman", 20, "bold"),bg="#1C1C1C",fg="cyan")
head_lable.grid(row=0,column=0)
head_title = Label(head_frame,text="Password Strength Checker",font=("Times New Roman", 10, "bold"),bg="#1C1C1C",fg="cyan")
head_title.grid(row=1,column=0)

pass_frame = Frame(base,bg="#1C1C1C")
pass_frame.pack(side=TOP,anchor="nw",padx=25,pady=10)

pass_lable = Label(pass_frame,text="Password:",font=("Times New Roman", 12),bg="#1C1C1C",fg="#F0F0F0")
pass_lable.grid(row=0,column=0)

passwordvar = StringVar()
passwordvar.set("")

password_entry = Entry(pass_frame,textvariable=passwordvar,font=("Times New Roman", 12),width=40)
password_entry.grid(row=0,column=1,padx=3)

check_frame = Frame(base)
check_frame.pack(side=TOP,anchor="center",pady=10)

check_button = Button(check_frame,text="Check",font=("Times New Roman", 12, "bold"),command=main,padx=10,bg="#2980B9",fg="#1C1C1C")
check_button.pack()

status_frame = Frame(base,bg="#1C1C1C")
status_frame.pack(side=TOP,anchor="center",pady=10)

status_lable = Label(status_frame,text="",font=("Times New Roman", 15, "bold"),bg="#1C1C1C")
status_lable.pack()

base.mainloop()
