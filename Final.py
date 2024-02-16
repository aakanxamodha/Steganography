from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root=Tk()
root.title("Steganography - The Secret behind the Secrets")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#352625")

def Select_image():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image File',
                                        filetype=(("PNG file","*.png"),
                                                  ("JPG File","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

def Encrypt():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename),message)
    tk.messagebox.showinfo("Done", "Encryption completed successfully!")
    text1.delete(1.0, END)
    
def Decrypt():
    clear_message = lsb.reveal(filename)
    text1.insert(END, clear_message)
    tk.messagebox.showinfo("Done", "Decryption completed successfully!")
    text1.delete(1.0, END)

def Save():
    secret.save("stegano_img.png")
    tk.messagebox.showinfo("Done", "Image downloaded successfully!")
    
#icon
image_icon=PhotoImage(file="Detector.png")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="Quiet_boy.png")
Label(root,image=logo,bg="#352625").place(x=10,y=0)

Label(root,text="DIGITAL FORENSICS - STEGNALYSIS",bg="#352625",fg="white",font="arial 23 bold").place(x=100,y=20)

#first frame
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

#second frame
frame2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=300)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third frame
frame3=Frame(root,bd=3,bg="#352625",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="Select Image",width=10,height=2,font="arial 14 bold",command=Select_image).place(x=20,y=30)
Button(frame3,text="Download",width=10,height=2,font="arial 14 bold",command=Save).place(x=180,y=30)
Label(frame3,text=".jpg/.jpeg/.png file",bg="#352625",fg="yellow").place(x=20,y=5)

#fourth frame
frame4=Frame(root,bd=3,bg="#352625",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Encrypt",width=10,height=2,font="arial 14 bold",command=Encrypt).place(x=20,y=30)
Button(frame4,text="Decrypt",width=10,height=2,font="arial 14 bold",command=Decrypt).place(x=180,y=30)
Label(frame4,text=".jpg/.jpeg/.png file",bg="#352625",fg="yellow").place(x=20,y=5)


root.mainloop()
