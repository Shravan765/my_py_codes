from tkinter import *



root = Tk()
root.title("TIMER APPLICATION")
root.geometry('1000x500')


exit_b = Button(root, text="EXIT", 
                   activebackground="blue", 
                   activeforeground="white",
                   disabledforeground="gray",
                   font=("Arial", 12),
                   command=root.destroy
                   )
exit_b.pack(anchor=SE)

a = Label(root, text = "This is a timer application\n")
a.config(font=("Times new roman", 20,"bold", "underline"))
a.pack()


b = Label( root, text = "Enter your time (seconds) below\n", font= ("ariel", 20))
b.pack()

quote = Label(root, text ="Time is more precious than money", font=("courier",15, "italic"))
quote.pack(side=BOTTOM,pady=50)

def is_int(val):
    return val.isdigit()
vcmd = root.register(is_int)
seconds = Entry(root, validate="key", validatecommand=(vcmd, "%S"))
seconds.pack()

def start():
    sec = seconds.get()
    sec = int(sec)
    lefttime = Label(root, text= "", font=("Times new roman", 20, "underline"))
    lefttime.pack(anchor=CENTER,pady=10)
    def update(count):
        if count>0:
            lefttime.config(text = str(count))
            root.after(1000, update, count-1)
        elif count == 0:
            lefttime.config(text = "DONE!")
            root.after(1000, update, count - 1)
        else:
            lefttime.config(text = "")
            lefttime.destroy()    
    update(sec)


submit = Button(root, text = "Start timer", command = start)
submit.pack()


#T = Text(root, height=10, width= 50, font=("courier",15, "italic"))







root.mainloop()