import pandas as pd
    
#Taking credits from the GUI
civil_credits=19.5
mech_credits=19.5
eee_credits=19.5
ece_credits=19.5
cse_credits=19.5
    
#Initializations
roll_no=0    #Variable for collectig last three digis of the RollNo
a=0    #
GPA=0.0
data=pd.read_excel("points.xlsx")
df=pd.DataFrame({"Roll_No":[]})
new=[]
    
#Deleting data frame for the creation of new branch dataframe with same name
def delete():
        global df
        d=df
        del df
        del d
        df=pd.DataFrame({"Roll_No":[]})
        print(len(df))
       
#Calculation and entering marks of the student into data frame
with pd.ExcelWriter('output.xlsx',engine = "openpyxl") as output:
    for i in range(len(data)):
    
        print(i,data['Htno'][i])
        d=str(data['Htno'][i])
        x=int(d[7:10])
        #start=d[1:5]
        
        #Entering the list of students values stored in the dataframe into the marks excel sheet
        if data['Htno'][i] not in new:
            def enter():  
                global a
                global roll_no
                global GPA
                if 'Grade Points' not in df.columns:
                    df['Grade Points']=[]        
                
                if ('F'  not in new) and ('AB' not in new):                                
                        GPA=GPA/total_credits                      
                                        
                else:
                    GPA="FAIL"
                new.append(GPA)
                print(new)
                print(a,'=',GPA)
                
                df.loc[len(df.index)]=new 
                
                new.clear()
                a=a+1
                GPA=0
                roll_no+=1
                
            if i>0:
                enter()
            new.append(data['Htno'][i])
        
        #Entering the excel sheets based on the branch (sheet1=Civil,sheet2=Mechanical,sheet3=EEE,sheet4=ECE,sheet5=CSE)
        if int(d[7])>(a/100):
            a=int(d[7])*100+1
            print("a=",a)
            if int(d[7])==1:
                total_credits=civil_credits
            if int(d[7])==2:
               
                data1=df.to_excel(output,sheet_name="civil",index=False)
                total_credits=mech_credits
                delete()
                df["Roll_No"]=[]
            if int(d[7])==3:
                
                data1=df.to_excel(output,sheet_name="Mechanical",index=False)
                total_credits=eee_credits
                delete()
                df["Roll_No"]=[]
            if int(d[7])==4:
                
                data1=df.to_excel(output,sheet_name='EEE',index=False)
                total_credits=ece_credits
                delete()
                df["Roll_No"]=[]
            if int(d[7])==5:
                
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
                GPA+=grade*data['Credits'][i]
                new.append(data['Grade'][i])
        elif data['Grade'][i]=='A':
                grade=9
                GPA+=grade*data['Credits'][i]
                new.append(data['Grade'][i])
        elif data['Grade'][i]=='B':
                grade=8
                GPA+=grade*data['Credits'][i]
                new.append(data['Grade'][i])
        elif data['Grade'][i]=='C':
                grade=7
                GPA+=grade*data['Credits'][i]
                new.append(data['Grade'][i])
        elif data['Grade'][i]=='D':
                grade=6
                GPA+=grade*data['Credits'][i]
                new.append(data['Grade'][i])
        elif data['Grade'][i]=='E':
                grade=5
                GPA+=grade*data['Credits'][i]
                new.append(data['Grade'][i])
        elif data['Grade'][i]=='F':             
                new.append(data['Grade'][i])
        elif data['Grade'][i]=='AB' or data['Grade'][i]=='ABSENT':
                new.append(data['Grade'][i])
        elif data['Grade'][i]=='COMPLETED' or data['Grade'][i]=='COMPLE':
                new.append(data['Grade'][i])
            
    #Adding final sheet CSE to the Excel
    data1=df.to_excel(output,sheet_name="CSE",index=False)