from pandas import *
from tkinter.filedialog import *
def excel_to_dataframe(data):
    civil=read_excel(data,sheet_name=["CE"])
    eee=read_excel(data,sheet_name=["EEE"])
    mech=read_excel(data,sheet_name=["ME"])
    ece=read_excel(data,sheet_name=["ECE"])
    cse=read_excel(data,sheet_name=["CSE"])
    return civil["CE"],eee["EEE"],mech["ME"],ece["ECE"],cse["CSE"]

def CGPA_cal(sem_selection,sem_file_list):    
    civil_final_df=DataFrame()
    eee_final_df=DataFrame()
    mech_final_df=DataFrame()
    ece_final_df=DataFrame()
    cse_final_df=DataFrame()
    
    def final_df_cal(final_df,df,i):
        df=df[["Roll_No","SGPA","Total Credits","Backlogs"]]
        df=df.rename(columns={"Total Credits":"Total Credits_sem"+str(i+1),"SGPA":"SGPA_sem"+str(i+1)})
        if len(final_df.columns)==0:
            final_df=df
        else:
            final_df=merge(final_df,df,"outer",on="Roll_No")
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
            except:
                return i+1
            if "Roll_No" not in civil_df.columns or "Total Credits" not in civil_df.columns or "SGPA" not in civil_df.columns or "Backlogs" not in civil_df.columns:
                return i+1
                
    def CGPA_calculations(df):   
        df["CGPA"]=0
        df["Total backlogs"]=0
        x=len(df.columns)//3-1
        value=0
        gpa=0
        backlogs=0
        for i in range(len(df)):
            for j in range(x):
                gpa+=(df.iloc[i,1+3*j])
                value+=(df.iloc[i,2+(3*j)])
                backlogs+=df.iloc[i,3+3*j]
            df.loc[i,"CGPA"]=gpa/value
            df.loc[i,"Total backlogs"]=backlogs
            value=0
            gpa=0
            backlogs=0
        df=df.drop(df.columns[3::3],axis=1)
        return df    
    civil_final_df=CGPA_calculations(civil_final_df)
    eee_final_df=CGPA_calculations(eee_final_df)
    mech_final_df=CGPA_calculations(mech_final_df)
    ece_final_df=CGPA_calculations(ece_final_df)
    cse_final_df=CGPA_calculations(cse_final_df)
    files=[('xlsx files','*.xlsx')]
    file=asksaveasfile(mode='wb',filetypes = files,defaultextension=files)
    with ExcelWriter(file,engine='openpyxl',mode='w') as output:
        civil_final_df.to_excel(output,sheet_name="Civil",index=False)
        eee_final_df.to_excel(output,sheet_name="EEE",index=False)
        mech_final_df.to_excel(output,sheet_name="Mechanical",index=False)
        ece_final_df.to_excel(output,sheet_name="ECE",index=False)
        cse_final_df.to_excel(output,sheet_name="CSE",index=False)
    return 0