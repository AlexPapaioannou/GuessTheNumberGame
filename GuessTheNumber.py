from tkinter import*
import random
import time
window=Tk()
window.title("Guess the number")
window.geometry("400x420")
window.configure(bg='black')
a=random.randint(0,100)

logo1=PhotoImage(file="UpArrow.png")
logo2=PhotoImage(file="DownArrow.png")
logo3=PhotoImage(file="Correct.png")

def check(event):
    global a,txt
    b=txt.get()
    if int(b)==a:
        lbl3.configure(image=logo3)
        txt.delete(0,END)
        txt.configure(state='disabled',bg='black')
    if int(b) > a:
        lbl3.configure(image=logo2)
        txt.delete(0,END)
    if int(b) < a:
        lbl3.configure(image=logo1)
        txt.delete(0,END)
def restart():
    global a,lbl3
    txt.configure(state='normal')
    for i in range(0, 15):
        a = random.randint(0, 100)
        lbl6.configure(text=a)
        lbl6.update()
        time.sleep(0.1)
    lbl6.configure(text="ready!")

lbl=Label(window,text="Guess the number ",bg='black',fg="#11FFF8",font=("Times New Roman",30))
lbl.grid(row=0,column=1,columnspan=3)
lbl2=Label(window,text="Find the secret number",bg='black',fg="#11FFF8",font=("Times New Roman",30))
lbl2.grid(row=2,column=1,columnspan=3)
txt=Entry(window,width=5,bg='black',fg="#11FFF8",font=("Times New Roman",30))
txt.grid(row=4,column=1,pady=30)
lbl3=Label(window,text="press")
lbl3=Label(window,text="enter",bg="black",fg="#11FFF8",font=("Times New Roman",20))
lbl3.grid(row=4,column=3)
btn=Button(window,text="Exit",command=exit,bg='grey',fg="#11FFF8",font=("Times New Roman",30))
btn.grid(row=6,column=1)
btn2=Button(window,text="Restart",bg='grey',fg="#11FFF8",font=("Times New Roman",30),command=restart)
btn2.grid(row=6,column=3)
lbl4=Label(window,text="",bg='black',fg="#11FFF8")
lbl4.grid(row=1,column=0)
lbl5=Label(window,text="",bg='black',fg="#11FFF8")
lbl5.grid(row=3,column=0)
lbl6=Label(window,text="",bg='black',fg="#11FFF8",font=("Times New Roman",20))
lbl6.grid(row=7,column=1,pady=20)




for i in range (0,15):
    a=random.randint(0,100)
    lbl6.configure(text=a)
    lbl6.update()
    time.sleep(0.1)
lbl6.configure(text="ready!")



window.bind('<Return>',check)
window.mainloop()