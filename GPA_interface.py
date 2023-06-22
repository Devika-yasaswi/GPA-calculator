from tkinter import *
from tkinter.filedialog import *
from regular_SGPA import *
from Revaluation import *
from PIL import Image, ImageTk
import tabula
input_file=''
GPA_file=''
master=Tk()
master.geometry("1000x850+300+0")
master.configure(bg="#1E90FF")
master.title("CGPA/SGPA Calculator")
img=PhotoImage(file="Background.png")
logo=Image.open("JNTUK logo.png")
new_logo=logo.resize((50,50))
new_logo=ImageTk.PhotoImage(new_logo)
my_canvas=Canvas(master,width=1000,height=750)
my_canvas.pack(fill='both',expand=True)
my_canvas.create_image(0,0,image=img,anchor="nw")
my_canvas.create_image(20,20,image=new_logo,anchor="nw")
my_canvas.create_text(70,20,text="University College of Engineering Narasaraopet",anchor="nw",font=('Algerian',25),fill="White")
my_canvas.create_text(350,60,text="CGPA/SGPA Calculator",anchor="nw",font=('Algerian',20),fill="White")
my_canvas.create_text(900,750,text="K. Devika Yasaswi",font=("Vladimir Script",18))
root=Frame(my_canvas,padx=20,pady=20,bg="#FFE9E3",highlightbackground="#F88F8F", highlightthickness=3)
root.configure()
root.pack(pady=110)

Label_font=('Times new Roman',20)   #Font style for labels
Entry_font=('Times new Roman',15)   #Font style for entry boxes
pdf_type = [("pdf Files",'.*pdf')]
excel_type=[("xlsx Files",".*xlsx")]
s_temp=0

#File reading function for SGPA-Regular
def input_marks_file():
    global input_file
    input_file=askopenfilename(filetypes=pdf_type)

#File reading function for SGPA-supple/Revaluation
def GPA_file_func():
    global GPA_file
    GPA_file=askopenfilename(filetypes=excel_type)
sem=IntVar()
def variable_sem_files():
    global sem_label_list,sem_button_list,s_temp
    try:
        if s_temp>sem.get():
            for i in range(sem.get(),s_temp):
                sem_label_list[i].grid_forget()
                sem_button_list[i].grid_forget()
    except FileNotFoundError:
        pass
    if sem.get()>=1 and sem.get()<=8:
        upload_sem_files()
        s_temp=sem.get()

def semester():
    global sem_select_label,sem1_cbutton,sem2_cbutton,sem3_cbutton,sem4_cbutton,sem5_cbutton,sem6_cbutton,sem7_cbutton,sem8_cbutton,sem
    sem_select_label=Label(root,text="Choose Semesters for CGPA",font=Label_font,bg="#FFE9E3")
    sem_select_label.grid(row=4,column=0,sticky='w')
    sem1_cbutton=Checkbutton(root,text="Sem 1",font=Entry_font,bg="#FFE9E3",command=variable_sem_files)
    sem1_cbutton.grid(row=4,column=2,sticky='w')
    sem2_cbutton=Checkbutton(root,text="Sem 2",font=Entry_font,bg="#FFE9E3",command=variable_sem_files)
    sem2_cbutton.grid(row=4,column=3,sticky='w')
    sem3_cbutton=Checkbutton(root,text="Sem 3",font=Entry_font,bg="#FFE9E3",command=variable_sem_files)
    sem3_cbutton.grid(row=5,column=2,sticky='w')
    sem4_cbutton=Checkbutton(root,text="Sem 4",font=Entry_font,bg="#FFE9E3",command=variable_sem_files)
    sem4_cbutton.grid(row=5,column=3,sticky='w')
    sem5_cbutton=Checkbutton(root,text="Sem 5",font=Entry_font,bg="#FFE9E3",command=variable_sem_files)
    sem5_cbutton.grid(row=6,column=2,sticky='w')
    sem6_cbutton=Checkbutton(root,text="Sem 6",font=Entry_font,bg="#FFE9E3",command=variable_sem_files)
    sem6_cbutton.grid(row=6,column=3,sticky='w')
    sem7_cbutton=Checkbutton(root,text="Sem 7",font=Entry_font,bg="#FFE9E3",command=variable_sem_files)
    sem7_cbutton.grid(row=7,column=2,sticky='w')
    sem8_cbutton=Checkbutton(root,text="Sem 8",font=Entry_font,bg="#FFE9E3",command=variable_sem_files)
    sem8_cbutton.grid(row=7,column=3,sticky='w')
#Sem SGPA file upload functions for CGPA calculation
def sem1_files():
    global sem1_file
    sem1_file=askopenfilename(filetypes=excel_type)
def sem2_files():
    global sem2_file
    sem2_file=askopenfilename(filetypes=excel_type)
def sem3_files():
    global sem3_file
    sem3_file=askopenfilename(filetypes=excel_type)
def sem4_files():
    global sem4_file
    sem4_file=askopenfilename(filetypes=excel_type)
def sem5_files():
    global sem5_file
    sem5_file=askopenfilename(filetypes=excel_type)
def sem6_files():
    global sem6_file
    sem6_file=askopenfilename(filetypes=excel_type)
def sem7_files():
    global sem7_file
    sem7_file=askopenfilename(filetypes=excel_type)
def sem8_files():
    global sem8_file
    sem8_file=askopenfilename(filetypes=excel_type)

sem1_sgpa=Label(root,text="Sem1 SGPA file",font=Entry_font,bg="#FFE9E3")
sem1_button=Button(root,text="Upload file",command=sem1_files)
sem2_sgpa=Label(root,text="Sem2 SGPA file",font=Entry_font,bg="#FFE9E3")
sem2_button=Button(root,text="Upload file",command=sem2_files)
sem3_sgpa=Label(root,text="Sem3 SGPA file",font=Entry_font,bg="#FFE9E3")
sem3_button=Button(root,text="Upload file",command=sem3_files)
sem4_sgpa=Label(root,text="Sem4 SGPA file",font=Entry_font,bg="#FFE9E3")
sem4_button=Button(root,text="Upload file",command=sem4_files)
sem5_sgpa=Label(root,text="Sem5 SGPA file",font=Entry_font,bg="#FFE9E3")
sem5_button=Button(root,text="Upload file",command=sem5_files)
sem6_sgpa=Label(root,text="Sem6 SGPA file",font=Entry_font,bg="#FFE9E3")
sem6_button=Button(root,text="Upload file",command=sem6_files)
sem7_sgpa=Label(root,text="Sem7 SGPA file",font=Entry_font,bg="#FFE9E3")
sem7_button=Button(root,text="Upload file",command=sem7_files)
sem8_sgpa=Label(root,text="Sem8 SGPA file",font=Entry_font,bg="#FFE9E3")
sem8_button=Button(root,text="Upload file",command=sem8_files)
#sem files uploading labels and buttons
def upload_sem_files():
    global sem,sem_label_list,sem_button_list
    r=8
    sem_label_list=[sem1_sgpa,sem2_sgpa,sem3_sgpa,sem4_sgpa,sem5_sgpa,sem6_sgpa,sem7_sgpa,sem8_sgpa]
    sem_button_list=[sem1_button,sem2_button,sem3_button,sem4_button,sem5_button,sem6_button,sem7_button,sem8_button]
    for i in range(sem.get()):
        sem_label_list[i].grid(row=r,column=0,sticky='w',pady=6)
        sem_button_list[i].grid(row=r,column=2,sticky='w')
        r+=1
C=IntVar()
S=IntVar()
def sem_type():
    global reval,reval_button,upload,upload_button
    if S.get()==2:
        reval=Label(root,text="Upload the previous GPA file",bg="#FFE9E3",font=Label_font)
        reval.grid(row=6,column=0,sticky='w')
        reval_button=Button(root, text='Upload File', width=20,command = GPA_file_func)
        reval_button.grid(row=6,column=2,sticky='w')
    elif S.get()==1:
        try:
            reval.grid_forget()
            reval_button.grid_forget()
        except:
            pass
    if S.get()==1 or S.get()==2:
        try:
            upload.grid_forget()
            upload_button.grid_forget()
        except:
            pass
        upload=Label(root,text="Upload the grades excel  ",bg="#FFE9E3",font=Label_font)
        upload.grid(row=5,column=0,sticky='w')
        upload_button=Button(root, text='Upload File', width=20,command = input_marks_file)
        upload_button.grid(row=5,column=2,sticky='w')
        credits()


def Cal_type():
    global semester_type,revalution,regular,upload,reval,reval_button,upload_button,sem_select_label,sem1_cbutton,sem2_cbutton,sem3_cbutton,sem4_cbutton,sem5_cbutton,sem6_cbutton,sem7_cbutton,sem8_cbutton
    
    if C.get()==1:            
        try:
            reval.grid_forget()
            reval_button.grid_forget()
        except:
            pass
        try:
            sem_select_label.grid_forget()
            sem1_cbutton.grid_forget()
            sem2_cbutton.grid_forget()
            sem3_cbutton.grid_forget()
            sem4_cbutton.grid_forget()
            sem5_cbutton.grid_forget()
            sem6_cbutton.grid_forget()
            sem7_cbutton.grid_forget()
            sem8_cbutton.grid_forget()
        except:
            pass
        try:
            for i in range(sem.get()):
                sem_label_list[i].grid_forget()
                sem_button_list[i].grid_forget()
        except:
            pass
        semester_type=Label(root,text="Semester Type",font=Label_font,bg="#FFE9E3")
        semester_type.grid(row=3,column=0,sticky='w')
        regular=Radiobutton(root,text="Regular",value=1,variable=S,font=Label_font,bg="#FFE9E3",command=sem_type)
        regular.grid(row=3,column=2,sticky='w')
        revalution=Radiobutton(root,text="Supplementary/Revaluation",value=2,variable=S,font=Label_font,bg="#FFE9E3",command=sem_type)
        revalution.grid(row=4,column=2,sticky='w')
    elif C.get()==2:
        try:
            semester()
            semester_type.grid_forget()
            regular.grid_forget()
            revalution.grid_forget()
            upload.grid_forget()
            upload_button.grid_forget() 
            reval.grid_forget()
            reval_button.grid_forget()                               
        except:
            pass

#Calculation type SGPA=1, CGPA=2
Label(root,text="Calculation Type",font=Label_font,bg="#FFE9E3").grid(row=1,column=0,sticky='w')
Radiobutton(root,text="SGPA",value=1,variable=C,font=Label_font,bg="#FFE9E3",command=Cal_type).grid(row=1,column=2,sticky='w')
Radiobutton(root,text="CGPA",value=2,variable=C,font=Label_font,bg="#FFE9E3",command=Cal_type).grid(row=2,column=2,sticky='w')   

#saving functionality
def save():
    global civil_credits,mech_credits,eee_credits,ece_credits,cse_credits,input_file,GPA_file   
    #checks calculation type selection
    if C.get()==1 or C.get()==2:
        #checks semester type selection
        if S.get()==1 or S.get()==2:  
            if C.get()==1:
                #checks input GPA file
                if input_file!='':                     
                    df=tabula.read_pdf(input_file,pages="all")
                    data=pd.DataFrame()
                    for i in range(len(df)):
                        data=pd.concat([data,df[i]],ignore_index=True)
                    if S.get()==2 and GPA_file=='':
                        Label(root,text='Please upload the previous GPA file',font=Entry_font,fg='red',bg="#FFE9E3").grid(row=20,column=0,sticky='w')
                    else:                    
                        if S.get()==1:
                            try:
                                rno_list=[]
                                for i in range(len(data)):
                                        x=int(data['Htno'][i][7:10])
                                        rno_list.append(data['Htno'][i][0:6])
                                new_rno_list=list(set(rno_list))
                                new=[]
                                for i in new_rno_list:
                                    new.append(rno_list.count(i))
                                series=new_rno_list[new.index(max(new))]
                                new_df=pd.DataFrame(columns=data.columns)
                                series1=str(int(series[0:2])+1)+"035A"
                                for i in range(len(data)):
                                    if data.iloc[i,0][0:6]== series or data.iloc[i,0][0:6]==series1:
                                        new_df.loc[len(new_df.index)]=list(data.iloc[i,:])
                                Sgpa(new_df)
                            except ValueError:
                                pass
                        else:
                            if S.get()==2:
                                reval_func(GPA_file,data)
                        master.destroy()
                        
                else:
                    Label(root,text='Please upload the grades excel',font=Entry_font,fg='red',bg="#FFE9E3").grid(row=20,column=0,sticky='w')
                #checks weather previous gpa file is uploaded or not
                
        else:
            Label(root,text='Please select Semester type    ',font=Entry_font,fg='red',bg="#FFE9E3").grid(row=20,column=0,sticky='w')
    else:
        Label(root,text='Please select Calculation type  ',font=Entry_font,fg='red',bg="#FFE9E3").grid(row=20,column=0,sticky='w')
    
#Reset functionality
def reset():
    master.destroy()
    student_data()
Label(root,text="  ",bg="#FFE9E3").grid(row=20,column=2)
#Get result button
Button(root,text="Get Result",command=save,font=('Times new Roman',18)).grid(row=21,column=2)
#Reset button
Button(root,text="Reset",command=reset,font=('Times new Roman',18)).grid(row=21,column=0)
master.mainloop()