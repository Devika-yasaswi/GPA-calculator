from tkinter import *
from tkinter.filedialog import *
from regular_SGPA import *
input_file=''
supple_file=''
def new():
    global gpa_supple,C,civil,mech,eee,ece,cse
    master=Tk()
    master.title("Application Form")
    master.geometry("1000x720+300+0")
    master.configure(bg="#ffa07a")
    master.title("CGPA/SGPA Calculator")
    Label(master,text="    ",bg="#ffa07a").pack() 
    Label(master,text="CGPA/SGPA Calculator",font=('Times new Roman',25,'italic'),bg="#ffa07a").pack() 
    root=Frame(padx=25,pady=25,bg="#ffdab9",highlightbackground="#ff8c69", highlightthickness=3)
    root.configure(bg="#ffdab9")
    root.pack()
    f_types = [('xlsx Files', '*.xlsx')]
    def marks_file():
        global input_file
        input_file=askopenfilename(filetypes=f_types)
    def supple_marks_file():
        global supple_file
        supple_file=askopenfilename(filetypes=f_types)
    Label(root,text="Upload the grades excel  ",bg="#ffdab9",font=('Times new Roman',20)).grid(row=1,column=0,sticky='w')
    Label(root,text="      ",bg="#ffdab9",font=('Times new Roman',20)).grid(row=1,column=1)
    Button(root, text='Upload File', width=20,command = marks_file).grid(row=1,column=2,sticky='w')
    C=IntVar()
    S=IntVar()
    gpa_supple=Label(root,text="Upload the previous GPA file(if any)",bg="#ffdab9",font=('Times new Roman',20))
    def sem_type():
        global reval,supple
        if S.get()==2:
            reval=Label(root,text="Upload the previous GPA file",bg="#ffdab9",font=('Times new Roman',20))
            reval.grid(row=6,column=0,sticky='w')
            supple=Button(root, text='Upload File', width=20,command = supple_marks_file)
            supple.grid(row=6,column=2,sticky='w')
        elif S.get()==1:
            try:
                reval.grid_forget()
                supple.grid_forget()
            except:
                pass
    def Cal_type():
        global semester,sup,reg,gpa_supple,reval,supple,cgpa
        
        if C.get()==1:
            try:
                gpa_supple.grid_forget()
                cgpa.grid_forget()
                reval.grid_forget()
                supple.grid_forget()
            except:
                pass
            semester=Label(root,text="Semester Type",font=('Times new Roman',20),bg="#ffdab9")
            semester.grid(row=4,column=0,sticky='w')
            reg=Radiobutton(root,text="Regular",value=1,variable=S,font=('Times new Roman',20),bg="#ffdab9",command=sem_type)
            reg.grid(row=4,column=2,sticky='w')
            sup=Radiobutton(root,text="Supplementary/Revaluation",value=2,variable=S,font=('Times new Roman',20),bg="#ffdab9",command=sem_type)
            sup.grid(row=5,column=2,sticky='w')
        elif C.get()==2:
            try:
                semester.grid_forget()
                reg.grid_forget()
                sup.grid_forget()
                reval.grid_forget()
                supple.grid_forget()
            except:
                pass
            gpa_supple.grid(row=4,column=0)
            cgpa=Button(root, text='Upload File', width=20,command = marks_file)
            cgpa.grid(row=4,column=2,sticky='w')
    
    #Calculation type
    Label(root,text="Calculation Type",font=('Times new Roman',20),bg="#ffdab9").grid(row=2,column=0,sticky='w')
    Radiobutton(root,text="SGPA",value=1,variable=C,font=('Times new Roman',20),bg="#ffdab9",command=Cal_type).grid(row=2,column=2,sticky='w')
    Radiobutton(root,text="CGPA",value=2,variable=C,font=('Times new Roman',20),bg="#ffdab9",command=Cal_type).grid(row=3,column=2,sticky='w')
   
    #Credit details labels and entries
    Label(root,text="***Enter total credits***",font=('Times new Roman',20),bg="#ffdab9").grid(row=12,column=0,sticky='w')
    civil=StringVar(root)
    Label(root,text="Civil",font=('Times new Roman',20),bg="#ffdab9").grid(row=13,column=0,sticky='w')
    Entry(root,font=('Times new Roman',15),textvariable=civil).grid(row=13,column=2,sticky='w')
    mech=StringVar(root)
    Label(root,text="Mechanical",font=('Times new Roman',20),bg="#ffdab9").grid(row=14,column=0,sticky='w')
    Entry(root,font=('Times new Roman',15),textvariable=mech).grid(row=14,column=2,sticky='w')
    eee=StringVar(root)
    Label(root,text="EEE",font=('Times new Roman',20),bg="#ffdab9").grid(row=15,column=0,sticky='w')
    Entry(root,font=('Times new Roman',15),textvariable=eee).grid(row=15,column=2,sticky='w')
    ece=StringVar(root)
    Label(root,text="ECE",font=('Times new Roman',20),bg="#ffdab9").grid(row=16,column=0,sticky='w')
    Entry(root,font=('Times new Roman',15),textvariable=ece).grid(row=16,column=2,sticky='w')
    cse=StringVar(root)
    Label(root,text="CSE",font=('Times new Roman',20),bg="#ffdab9").grid(row=17,column=0,sticky='w')
    Entry(root,font=('Times new Roman',15),textvariable=cse).grid(row=17,column=2,sticky='w')
    Label(root,text="  ",bg="#ffdab9").grid(row=19,column=1,sticky='w')

    #saving functionality
    def save():
        global civil_credits,mech_credits,eee_credits,ece_credits,cse_credits,input_file,supple_file,civil,mech,ece,cse,eee
        #checks input GPA file
        if input_file!='': 
            #checks calculation type selection
            if C.get()==1 or C.get()==2:
                #checks semester type selection
                if S.get()==1 or S.get()==2:  
                    #checks weather previous gpa file is uploaded or not
                    if S.get()==2 and supple_file=='':
                        Label(root,text='Please upload the previous GPA file',font=('Times new Roman',15),fg='red',bg="#ffdab9").grid(row=20,column=0,sticky='w')
                    else:
                        print("Hello")
                        try:
                            print("try")
                            print(civil.get(),":",mech.get(),":",eee.get(),":",ece.get(),":",cse.get())
                            civil_credits=float(civil.get())
                            mech_credits=float(mech.get())
                            eee_credits=float(eee.get())
                            ece_credits=float(ece.get())
                            cse_credits=float(cse.get())
                            if C.get()==1:
                                try:
                                    Sgpa(civil_credits,mech_credits,eee_credits,ece_credits,cse_credits,input_file)
                                except ValueError:
                                    pass
                            else:
                                if S.get()==1:
                                    pass
                                else:
                                    pass
                            master.destroy()
                        except FileNotFoundError:
                            Label(root,text='Please enter total credits of all branches correctly',font=('Times new Roman',15),fg='red',bg="#ffdab9").grid(row=20,column=0,sticky='w')
                else:
                    Label(root,text='Please select Semester type    ',font=('Times new Roman',15),fg='red',bg="#ffdab9").grid(row=20,column=0,sticky='w')
            else:
                Label(root,text='Please select Calculation type  ',font=('Times new Roman',15),fg='red',bg="#ffdab9").grid(row=20,column=0,sticky='w')
        else:
            Label(root,text='Please upload the grades excel',font=('Times new Roman',15),fg='red',bg="#ffdab9").grid(row=20,column=0,sticky='w')
    #Reset functionality
    def reset():
        master.destroy()
        new()
    #Get result button
    Button(root,text="Get Result",command=save,font=('Times new Roman',18)).grid(row=21,column=2)
    #Reset button
    Button(root,text="Reset",command=reset,font=('Times new Roman',18)).grid(row=21,column=0)
    master.mainloop()
new()