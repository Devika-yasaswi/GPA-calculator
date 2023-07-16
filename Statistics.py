from pandas import *
from tkinter.filedialog import *
from openpyxl import load_workbook
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