import pandas as pd
from tkinter.filedialog import *
def Sgpa(data):
    #Initializations
    global GPA,a,roll_no,student_data,start,start_x,df,civil_credits,eee_credits,mech_credits,ece_credits,cse_credits,GBM
    roll_no=0    #Variable for collectig last three digis of the RollNo
    a=0    #
    GPA=0.0
    df=pd.DataFrame({"Roll_No":[]})
    student_data=[data['Htno'][1]]
    sub=[]
    start=int(data['Htno'][1][0:4])  
    start_x=1
    cse=0
    total=0
    civil_credits=0
    eee_credits=0
    mech_credits=0
    ece_credits=0
    cse_credits=0
    GBM=0
    rno_list=[]

    #Deleting data frame for the creation of new branch dataframe with same name
    def delete():
            global df
            d=df
            del df
            del d
            df=pd.DataFrame({"Roll_No":[]})
            print(len(df))
        
    #Calculation and entering marks of the student into data frame
    files=[('xlsx files','*.xlsx')]
    file=asksaveasfile(mode='wb',filetypes = files,defaultextension=files)

    #Calculating credits
    for i in range(len(data)):
        x=int(data['Htno'][i][7:10])
        rno_list.append(data['Htno'][i][0:6])
        if data['Subcode'][i] not in sub:
            sub.append(data['Subcode'][i])
            total+=float(data['Credits'][i])
            student_data.append(data['Grade'][i])
        if data['Htno'][i] not in student_data:
            if x//100==1:
                if "MP" not in student_data and 'F' not in student_data and "AB" not in student_data:
                     civil_credits=total
            elif x//100==2:
                if "MP" not in student_data and 'F' not in student_data and "AB" not in student_data:
                     eee_credits=total
            elif x//100==3:
                if "MP" not in student_data and 'F' not in student_data and "AB" not in student_data:
                     mech_credits=total
            elif x//100==4:
                if "MP" not in student_data and 'F' not in student_data and "AB" not in student_data:
                     ece_credits=total
            elif x//100==5:
                if "MP" not in student_data and 'F' not in student_data and "AB" not in student_data:
                     cse_credits=total
            print(student_data)
            print(x," ",civil_credits," ",eee_credits," ",mech_credits," ",ece_credits," ",cse_credits)
            sub=[]
            total=0
            student_data=[data['Htno'][i]]        
    print(civil_credits," ",eee_credits," ",mech_credits," ",ece_credits," ",cse_credits)
    student_data=[]
    #calculating and writing GPA to output file
    with pd.ExcelWriter(file.name,engine='openpyxl',mode='w') as output:
    
        for i in range(len(data)):
        
            print(i,data['Htno'][i])
            d=str(data['Htno'][i])
            x=int(d[7:10])
                    
            #Entering the list of students values stored in the dataframe into the marks excel sheet
            if data['Htno'][i] not in student_data:
                def enter():  
                    global a,roll_no,GPA,GBM
                    if 'Points' not in df.columns:
                        df['GBM']=[]
                        df['Total Credits']=[] 
                        df['Status']=[]
                        df['Backlogs']=[]
                        df['Pass Percentage']=[]
                        df['SGPA']=[]
                        df['Points']=[]
                    student_data.append(GBM)    
                    
                    student_data.append(total_credits)
                    if "F" not in student_data and "AB" not in student_data and "MP" not in student_data:
                        student_data.append("Pass")
                    else:
                        student_data.append("Fail")
                    student_data.append(student_data.count("F")+student_data.count("AB")+student_data.count("MP")+student_data.count("ABSENT"))
                    student_data.append(GBM/(len(sub)-(student_data.count("COMPLE")+student_data.count("COMPLETED"))))
                    student_data.append(GPA)                       
                    GPA=GPA/total_credits                 
                    student_data.append(GPA)                    
                    print(student_data)
                    print(a,'=',GPA)
                    
                    df.loc[len(df.index)]=student_data 
                    
                    student_data.clear()
                    a=a+1
                    GPA=0
                    roll_no+=1
                    GBM=0
                if i>0:
                    enter()
                student_data.append(data['Htno'][i])
            
            #Entering the excel sheets based on the branch (sheet1=Civil,sheet2=Mechanical,sheet3=EEE,sheet4=ECE,sheet5=CSE)
            if int(d[7])>(a/100) or int(d[0:4])>start:
                if int(d[0:4])>start:
                    start=int(d[0:4])
                    cse=len(df.index)+1
                    data1=df.to_excel(output,sheet_name="CSE",index=False)
                    start_x=2
                    delete()
                a=int(d[7])*100+1
                print("a=",a)
                if int(d[7])==1:
                    total_credits=civil_credits
                if int(d[7])==2:
                    
                    if start_x==2:
                        data1=df.to_excel(output,sheet_name="Civil",index=False,startrow=civil,header=None)
                    else:
                        civil=len(df.index)+1
                        data1=df.to_excel(output,sheet_name="Civil",index=False)
                    total_credits=eee_credits
                    delete()
                    df["Roll_No"]=[]
                if int(d[7])==3:
                    if start_x==2:
                        data1=df.to_excel(output,sheet_name="EEE",index=False,startrow=eee,header=None)
                    else:
                        eee=len(df.index)+1
                        data1=df.to_excel(output,sheet_name="EEE",index=False)
                    total_credits=mech_credits
                    delete()
                    df["Roll_No"]=[]
                if int(d[7])==4:
                    if start_x==2:
                        data1=df.to_excel(output,sheet_name="Mechanical",index=False,startrow=mech,header=None)
                    else:
                        mech=len(df.index)+1
                        data1=df.to_excel(output,sheet_name='Mechanical',index=False)
                    total_credits=ece_credits
                    delete()
                    df["Roll_No"]=[]
                if int(d[7])==5:
                    if start_x==2:
                        data1=df.to_excel(output,sheet_name="ECE",index=False,startrow=ece,header=None)
                    else:
                        ece=len(df.index)+1
                        data1=df.to_excel(output,sheet_name="ECE",index=False)
                    total_credits=cse_credits
                    delete()
                    df["Roll_No"]=[]
                sub=[]
        
        #Adding subject name columns in the dataframe based on the subject code
            if data['Subcode'][i] not in sub:
                
                sub.append(data['Subcode'][i])
                df[data['Subname'][i]+' ('+data['Subcode'][i]+')']=[]

            
            #Grades acquired based on the marks of the students 
            #90-100  A+ grade
            #80-89  A grade
            #70-79  B grade
            #60-69  C grade
            #50-59  D grade
            #40-59  E grade
            #<40 Fail
            #AB Absent
            if data['Grade'][i]=='A+':
                    grade=10
                    GBM+=grade*10
                    GPA+=grade*data['Credits'][i]
                    student_data.append(data['Grade'][i])
            elif data['Grade'][i]=='A':
                    grade=9
                    GBM+=grade*10
                    GPA+=grade*data['Credits'][i]
                    student_data.append(data['Grade'][i])
            elif data['Grade'][i]=='B':
                    grade=8
                    GBM+=grade*10
                    GPA+=grade*data['Credits'][i]
                    student_data.append(data['Grade'][i])
            elif data['Grade'][i]=='C':
                    grade=7
                    GBM+=grade*10
                    GPA+=grade*data['Credits'][i]
                    student_data.append(data['Grade'][i])
            elif data['Grade'][i]=='D':
                    grade=6
                    GBM+=grade*10
                    GPA+=grade*data['Credits'][i]
                    student_data.append(data['Grade'][i])
            elif data['Grade'][i]=='E':
                    grade=5
                    GBM+=grade*10
                    GPA+=grade*data['Credits'][i]
                    student_data.append(data['Grade'][i])
            elif data['Grade'][i]=='F':             
                    student_data.append(data['Grade'][i])
            elif data['Grade'][i]=='AB' or data['Grade'][i]=='ABSENT' or data['Grade'][i]=="MP":
                    student_data.append(data['Grade'][i])
            elif data['Grade'][i]=='COMPLETED' or data['Grade'][i]=='COMPLE':
                    student_data.append(data['Grade'][i])
                
        #Adding final sheet CSE to the Excel
        enter()
        if start_x==2:
            data1=df.to_excel(output,sheet_name="CSE",index=False,startrow=cse,header=None)
        else:
                data1=df.to_excel(output,sheet_name="CSE",index=False,startrow=cse)