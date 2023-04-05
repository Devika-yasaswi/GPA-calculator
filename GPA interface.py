from tkinter import *
from openpyxl import *



def new():
    master=Tk()
    master.title("Application Form")

    master.geometry("1000x1000")
    master.configure(bg="#ffa07a")
    master.title("CGPA/SGPA Calculator")
    Label(master,text="University college of Engineering Narsaraopet,JNTUK",font=('Times new Roman',20,'italic'),bg="#ffa07a").pack()  
    Label(master,text="CGPA/SGPA Calculator",font=('Times new Roman',20,'italic'),bg="#ffa07a").pack()  
    my_canvas=Canvas(master,width=700,bg="#ffdab9",highlightbackground="#ff8c69", highlightthickness=3)

    my_canvas.pack(side=LEFT,fill=Y,expand=1)

    my_scrollbar=Scrollbar(master,orient=VERTICAL,command=my_canvas.yview)

    my_scrollbar.pack(side=RIGHT,fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)

    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    root=Frame(my_canvas)
    root.configure(bg="#ffdab9")
    my_canvas.create_window((100,100),window=root,anchor="nw")
    Label(root,text="Address of the marks excel  ",bg="#ffdab9",font=('Times new Roman',20)).grid(row=1,column=1)
    marks_add=StringVar(root)
    Entry(root,font=('Times new Roman',15),textvariable=marks_add).grid(row=1,column=2)
    s=IntVar()
    t=IntVar()
    Label(root,text="Semester Type",font=('Times new Roman',20),bg="#ffdab9").grid(row=2,column=1,sticky='w')
    Radiobutton(root,text="Regular",value=1,variable=t,font=('Times new Roman',20),bg="#ffdab9").grid(row=2,column=2,sticky='w')
    Radiobutton(root,text="Supplementary",value=2,variable=t,font=('Times new Roman',20),bg="#ffdab9").grid(row=3,column=2,sticky='w')
    Label(root,text="Semester",font=('Times new Roman',20),bg="#ffdab9").grid(row=4,column=1,sticky='w')
    Radiobutton(root,text="Sem 1",value=1,variable=s,font=('Times new Roman',20),bg="#ffdab9").grid(row=4,column=2,sticky='w')
    Radiobutton(root,text="Sem 2",value=2,variable=s,font=('Times new Roman',20),bg="#ffdab9").grid(row=5,column=2,sticky='w')
    Radiobutton(root,text="Sem 3",value=3,variable=s,font=('Times new Roman',20),bg="#ffdab9").grid(row=6,column=2,sticky='w')
    Radiobutton(root,text="Sem 4",value=4,variable=s,font=('Times new Roman',20),bg="#ffdab9").grid(row=7,column=2,sticky='w')
    Radiobutton(root,text="Sem 5",value=5,variable=s,font=('Times new Roman',20),bg="#ffdab9").grid(row=8,column=2,sticky='w')
    Radiobutton(root,text="Sem 6",value=6,variable=s,font=('Times new Roman',20),bg="#ffdab9").grid(row=9,column=2,sticky='w')
    Radiobutton(root,text="Sem 7",value=7,variable=s,font=('Times new Roman',20),bg="#ffdab9").grid(row=10,column=2,sticky='w')
    Radiobutton(root,text="Sem 8",value=8,variable=s,font=('Times new Roman',20),bg="#ffdab9").grid(row=11,column=2,sticky='w')
    Label(root,text="***Enter total credits***",font=('Times new Roman',20),bg="#ffdab9").grid(row=12,column=1,sticky='w')
    civil=StringVar(root)
    Label(root,text="Civil",font=('Times new Roman',20),bg="#ffdab9").grid(row=13,column=1,sticky='w')
    Entry(root,font=('Times new Roman',15)).grid(row=13,column=2,sticky='w')
    mech=StringVar(root)
    Label(root,text="Mechanical",font=('Times new Roman',20),bg="#ffdab9").grid(row=14,column=1,sticky='w')
    Entry(root,font=('Times new Roman',15),textvariable=mech).grid(row=14,column=2,sticky='w')
    eee=StringVar(root)
    Label(root,text="EEE",font=('Times new Roman',20),bg="#ffdab9").grid(row=15,column=1,sticky='w')
    Entry(root,font=('Times new Roman',15),textvariable=eee).grid(row=15,column=2,sticky='w')
    ece=StringVar(root)
    Label(root,text="ECE",font=('Times new Roman',20),bg="#ffdab9").grid(row=16,column=1,sticky='w')
    Entry(root,font=('Times new Roman',15),textvariable=ece).grid(row=16,column=2,sticky='w')
    cse=StringVar(root)
    Label(root,text="CSE",font=('Times new Roman',20),bg="#ffdab9").grid(row=17,column=1,sticky='w')
    Entry(root,font=('Times new Roman',15),textvariable=cse).grid(row=17,column=2,sticky='w')
    save_add=StringVar(root)
    Label(root,text="Address of GPA excel",font=('Times new Roman',20),bg="#ffdab9").grid(row=18,column=1,sticky='w')
    Entry(root,textvariable=save_add,font=('Times new Roman',15)).grid(row=18,column=2,sticky='w')
    Label(root,text="  ",bg="#ffdab9").grid(row=19,column=1,sticky='w')
    def save():
        file_add=marks_add.get()
        sem=s.get()
        civil_credits=civil.get()
        mech_credits=mech.get()
        eee_credits=eee.get()
        ece_credits=ece.get()
        cse_credits=cse.get()
        save_file=save_add.get()
        master.destroy()
    def new():
        master.destroy()
        
    Button(root,text="Submit",command=save,font=('Times new Roman',18)).grid(row=21,column=1)
    Button(root,text="Reset",command=new,font=('Times new Roman',18)).grid(row=21,column=2)
    Label(root,text="  ",bg="#ffdab9").grid(row=22,column=1,sticky='w')
    Label(root,text="  ",bg="#ffdab9").grid(row=23,column=1,sticky='w')
    master.mainloop()

new()



 
