from pandas import *
from tkinter.filedialog import *
def branch_calculation(data):
    df=DataFrame(columns=["subject","No.of students registered","No.of students appeared","Absentees","Pass Percentage"])
    for i in list(data.columns)[1:-7]:
        temp_list=[i]
        sub=data[i].tolist()
        temp_list.append(len(sub))
        total=len(sub)-(sub.count("AB")+sub.count("ABSENT"))
        temp_list.append(total)
        temp_list.append(sub.count("AB")+sub.count("ABSENT"))
        passed=sub.count("A+")+sub.count("A")+sub.count("B")+sub.count("C")+sub.count("D")+sub.count("E")+sub.count("COMPLE")+sub.count("COMPLETED")
        temp_list.append(passed/total*100)
        df.loc[len(df.index)]=temp_list
    count=0
    count1=0
    for i in range(len(data)):
        new=data.iloc[i,1:-7]    
        new=list(set(new))
        if len(new)==1 and (new[0]=="AB" or new[i]=="ABSENT"):
            count+=1
        if len(new)!=1 and ("F" in new or "MP" in new or  "AB" in new or "ABSENT" in new or "MP" in new):
            count1+=1
    df1=DataFrame(columns=["Total no.of students","No.of students appeared","Pass percentage"])
    new=[len(data),len(data)-count,(len(data)-count-count1)/(len(data)-count)*100]
    df1.loc[len(df1.index)]=new
    data=data.sort_values(by=["Points"])
    df2=DataFrame(columns=["Place","Roll No","Points","SGPA"])
    x=1
    temp=data.iloc[-1,-1]
    for i in range(1,len(data)):
        if x<3 or temp==data.iloc[-i,-1]:
            if temp!=data.iloc[-i,-1]:
                x+=1
            new=[x,data.iloc[-i,0],data.iloc[-i,-2],data.iloc[-i,-1]]
            temp=data.iloc[-i,-1]
            df2.loc[len(df2.index)]=new     
        elif x==3:
            break
    df=concat([df,df1,df2],axis=1)
    return df
    

def get_statistics(file):
    civil_data=read_excel(file,sheet_name=["CE"])
    civil_data=DataFrame(civil_data["CE"])
    eee_data=read_excel(file,sheet_name=["EEE"])
    eee_data=eee_data["EEE"]
    mech_data=read_excel(file,sheet_name=["ME"])
    mech_data=mech_data["ME"]
    ece_data=read_excel(file,sheet_name=["ECE"])
    ece_data=ece_data["ECE"]
    cse_data=read_excel(file,sheet_name=["CSE"])
    cse_data=cse_data["CSE"]
    civil_data=branch_calculation(civil_data)
    eee_data=branch_calculation(eee_data)
    mech_data=branch_calculation(mech_data)
    ece_data=branch_calculation(ece_data)
    cse_data=branch_calculation(cse_data)
    with ExcelWriter(file,engine='openpyxl',mode='a',if_sheet_exists="replace") as output:
        civil_data.to_excel(output,sheet_name="CE stats",index=False)
        eee_data.to_excel(output,sheet_name="EEE stats",index=False)
        mech_data.to_excel(output,sheet_name="ME stats",index=False)
        ece_data.to_excel(output,sheet_name="ECE stats",index=False)
        cse_data.to_excel(output,sheet_name="CSE stats",index=False)