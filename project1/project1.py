from tkinter import*
from tkinter import ttk
from tkinter.filedialog import*
from tkinter import scrolledtext
from tkinter.filedialog import*
import sys
from tkinter.messagebox import*
N=8
texts=["Esimene","Teine","Kolmas","Neljas","Viies","Kuues","Seitsmes","Kaheksas"]
def phonk():
    #a=m1.selection_get()
    if a==0:
        tabs.select(0)
    elif a==1:
        tabs.select(1)
    elif a==2:
        tabs.select(2)
def open_():
    file=askopenfilename()
    for text in fileinput.input(file):
        txtbox.insert(0.0,text)
def save_():
    file=asksaveasfile(mode="w",defaultextension=((".txt"),(".docx")),filetypes=(("Notepad",".txt"),("Word",".docx")))
    t=txtbox.get(0.0,END)
    file.write(t)
    file.close()
def exit_():
    if askyesno("Exit","Yes/No"):
        showinfo("Exit","Message: Yes")
        root.destroy()
    else:
         showinfo("No")
root=Tk()
root.geometry("400x300")
root.title("Elemendid Tkinteris")
tabs=ttk.Notebook(root)
tab1=Frame(tabs)
#tab2=Frame(tabs)
#tab3=Frame(tabs)
#tab4=Frame(tabs)
#tabs.add(tab1,text="Esimene")
#tabs.add(tab2,text="Teine")
#tabs.add(tab3,text="Kolmas")
#tabs.add(tab4,text="Neljas")
#tabslist=[[Frame,str]]
#for i in range(1,N+1):
#    t="tab"+str(i)
#    tab=Frame(tabs)
#    tabs.add(tab,text=texts[i])
M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Menu1",menu=m1)
m1.add_command(label="Com1",command=phonk)
m1.add_command(label="Com2",command=phonk)
m1.add_command(label="Com3",command=phonk)
m1.add_command(label="Com4",command=phonk)
m2=Menu(M,tearoff=1)
M.add_cascade(label="BG Colors",menu=m2)
m2.add_command(label="Yellow",command=lambda:root.config(bg="yellow"))
m2.add_command(label="Green",command=lambda:root.config(bg="green"))
m2.add_command(label="Blue",command=lambda:root.config(bg="blue"))
m2.add_command(label="Purple",command=lambda:root.config(bg="purple"))
tabs.pack(fill="both")
m3=Menu(M,tearoff=1)
M.add_cascade(label="Window Size",menu=m3)
m3.add_command(label="Small",command=lambda:root.geometry("200x100"))
m3.add_command(label="Medium",command=lambda:root.geometry("400x300"))
m3.add_command(label="Large",command=lambda:root.geometry("600x500"))
btnopen=Button(tab1,text="Open")
btnsave=Button(tab1,text="Save")
btnexit=Button(tab1,text="Exit")
txtbox=scrolledtext
txtbox=Text(tab1)
txtbox.grid(row=0,column=0,columnspan=3)
btnopen.grid(row=1,column=1)
btnsave.grid(row=1,column=1)
btnexit.grid(row=1,column=2)
root.mainloop()