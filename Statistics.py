from pandas import *
from tkinter.filedialog import *
def branch_calculation(data):
    df=DataFrame(columns=["Subject","A+","A","B","C","D","E","F","ABSENT","MP","COMPLETED"])
    for i in list(data.columns)[1:-7]:
        temp_list=[]
        sub=data[i].tolist()
        temp_list.append(i)
        temp_list.append(sub.count("A+"))
        temp_list.append(sub.count("A"))
        temp_list.append(sub.count("B"))
        temp_list.append(sub.count("C"))
        temp_list.append(sub.count("D"))
        temp_list.append(sub.count("E"))
        temp_list.append(sub.count("F"))
        temp_list.append(sub.count("AB")+sub.count("ABSENT"))
        temp_list.append(sub.count("MP"))
        temp_list.append(sub.count("COMPLE")+sub.count("COMPLETED"))
        df.loc[len(df.index)]=temp_list
    return df
def get_statistics(file):
    civil_data=read_excel(file,sheet_name=["Civil"])
    civil_data=DataFrame(civil_data["Civil"])
    eee_data=read_excel(file,sheet_name=["EEE"])
    eee_data=eee_data["EEE"]
    mech_data=read_excel(file,sheet_name=["Mechanical"])
    mech_data=mech_data["Mechanical"]
    ece_data=read_excel(file,sheet_name=["ECE"])
    ece_data=ece_data["ECE"]
    cse_data=read_excel(file,sheet_name=["CSE"])
    cse_data=cse_data["CSE"]
    if "Points" not in list(civil_data.columns):
        return 1
    files=[('xlsx files','*.xlsx')]
    output_file=asksaveasfile(mode='wb',filetypes = files,defaultextension=files)
    civil_data=branch_calculation(civil_data)
    eee_data=branch_calculation(eee_data)
    mech_data=branch_calculation(mech_data)
    ece_data=branch_calculation(ece_data)
    cse_data=branch_calculation(cse_data)
    with ExcelWriter(output_file,engine='openpyxl',mode='w') as output:
        civil_data.to_excel(output,sheet_name="Civil",index=False)
        eee_data.to_excel(output,sheet_name="EEE",index=False)
        mech_data.to_excel(output,sheet_name="Mechanical",index=False)
        ece_data.to_excel(output,sheet_name="ECE",index=False)
        cse_data.to_excel(output,sheet_name="CSE",index=False)
    return 0