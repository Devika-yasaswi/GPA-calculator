from pandas import *
from tkinter.filedialog import *
def excel_to_dataframe(data):
    civil=read_excel(data,sheet_name=["Civil"])
    eee=read_excel(data,sheet_name=["EEE"])
    mech=read_excel(data,sheet_name=["Mechanical"])
    ece=read_excel(data,sheet_name=["ECE"])
    cse=read_excel(data,sheet_name=["CSE"])
    return civil["Civil"],eee["EEE"],mech["Mechanical"],ece["ECE"],cse["CSE"]

def CGPA_cal(sem_selection,sem_file_list):    
    civil_final_df=DataFrame()
    eee_final_df=DataFrame()
    mech_final_df=DataFrame()
    ece_final_df=DataFrame()
    cse_final_df=DataFrame()
    
    def final_df_cal(final_df,df,i):
        df=df[["Roll No","Points","Total Credits","SGPA","Backlogs"]]
        df=df.rename(columns={"Total Credits":"Total Credits sem"+str(i+1),"Points":"Points sem"+str(i+1),"SGPA":"SGPA sem"+str(i+1)})
        if len(final_df.columns)==0:
            final_df=df
        else:
            final_df=merge(final_df,df,"outer",on="Roll No")
        final_df=final_df.fillna(0)
        return final_df
    for i in range(len(sem_selection)):
        if sem_selection[i]==1:
            try:
                civil_df,eee_df,mech_df,ece_df,cse_df=excel_to_dataframe(sem_file_list[i])
                civil_final_df=final_df_cal(civil_final_df,civil_df,i)
                eee_final_df=final_df_cal(eee_final_df,eee_df,i)
                mech_final_df=final_df_cal(mech_final_df,mech_df,i)
                ece_final_df=final_df_cal(ece_final_df,ece_df,i)
                cse_final_df=final_df_cal(cse_final_df,cse_df,i)
            except :
                return i+1
            if "Roll No" not in civil_df.columns or "Total Credits" not in civil_df.columns or "SGPA" not in civil_df.columns or "Backlogs" not in civil_df.columns:
                return i+1
                
    def CGPA_calculations(df):   
        df["CGPA"]=0
        df["Total backlogs"]=0
        x=len(df.columns)//4
        value=0
        gpa=0
        backlogs=0
        for i in range(len(df)):
            for j in range(x):
                gpa+=(df.iloc[i,1+4*j])
                value+=(df.iloc[i,2+(4*j)])
                backlogs+=df.iloc[i,4+(4*j)]
            df.loc[i,"CGPA"]=gpa/value
            df.loc[i,"Total backlogs"]=backlogs
            value=0
            gpa=0
            backlogs=0
        df=df.drop(df.columns[4::4],axis=1)
        return df    
    civil_final_df=CGPA_calculations(civil_final_df)
    eee_final_df=CGPA_calculations(eee_final_df)
    mech_final_df=CGPA_calculations(mech_final_df)
    ece_final_df=CGPA_calculations(ece_final_df)
    cse_final_df=CGPA_calculations(cse_final_df)
    files=[('xlsx files','*.xlsx')]
    file=asksaveasfile(mode='wb',filetypes = files,defaultextension=files)
    with ExcelWriter(file,engine='openpyxl',mode='w') as output:
        try:
            civil_final_df.to_excel(output,sheet_name="Civil",index=False)
        except:
            pass
        try:
            eee_final_df.to_excel(output,sheet_name="EEE",index=False)
        except:
            pass
        try:
            mech_final_df.to_excel(output,sheet_name="Mechanical",index=False)
        except:
            pass
        try:
            ece_final_df.to_excel(output,sheet_name="ECE",index=False)
        except:
            pass
        try:
            cse_final_df.to_excel(output,sheet_name="CSE",index=False)
        except:
            pass
    return 0