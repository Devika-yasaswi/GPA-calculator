from tkinter import *
def user_guide():
    user=Toplevel()
    user.geometry("1200x800+300+0")
    user.title("User Guide")
    user.configure(bg="#FFE9E3")    
    my_canvas=Canvas(user,width=1160)
    my_canvas.pack(side=LEFT,fill=Y,expand=1,padx=10)
    my_scrollbar=Scrollbar(user,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    my_canvas.configure(bg="#FFE9E3")
    #my_canvas.pack(fill='both',expand=True)
    new_root=Frame(my_canvas)
    new_root.configure(bg="#FFE9E3")
    my_canvas.create_window((0,0),window=new_root,anchor="nw")
    head_font=('Times new Roman',18,'bold',"italic")   #Font style for headings
    body_font=('Times new Roman',15)
    spl_body_font=('Times new Roman',15,'bold')
    #Label(new_root,text="User Guide: SGPA and CGPA Calculation Tool",font=head_font,bg="#FFE9E3").grid(row=0,column=1,sticky='nw')
    Label(new_root,text="This user guide provides step-by-step instructions on how to use the GPA calculation tool to obtain and analyze ",font=body_font,bg="#FFE9E3").grid(row=1,column=1,sticky='nw')
    Label(new_root,text="student results for a semester.",font=body_font,bg="#FFE9E3").grid(row=2,column=1,sticky='nw')
    Label(new_root,text="Selecting Calculation Mode:",font=head_font,bg="#FFE9E3").grid(row=3,column=1,sticky='nw')
    Label(new_root,text="* To calculate the total GPA of a class for a semester, select the 'SGPA' option.",font=body_font,bg="#FFE9E3").grid(row=4,column=1,sticky='nw')
    Label(new_root,text="* To calculate the CGPA of the class, choose the 'CGPA' option.",font=body_font,bg="#FFE9E3").grid(row=5,column=1,sticky='nw')
    Label(new_root,text="Calculating and Saving SGPA",font=head_font,bg="#FFE9E3").grid(row=6,column=1,sticky='nw')
    Label(new_root,text="* For regular results, choose 'Regular'.",font=body_font,bg="#FFE9E3").grid(row=7,column=1,sticky='nw')
    Label(new_root,text="* If you wish to update regular results with supplementary or revaluation results, opt for 'Revaluation/Supplementary'.",font=body_font,bg="#FFE9E3").grid(row=8,column=1,sticky='nw')
    Label(new_root,text="1)For regular results:",font=spl_body_font,bg="#FFE9E3").grid(row=9,column=1,sticky='nw')
    Label(new_root,text="  * Upload the regular result PDF provided by the university and click on submit.",font=body_font,bg="#FFE9E3").grid(row=10,column=1,sticky='nw')
    Label(new_root,text="  * Browse and choose the location where you want to save the calculated GPA file.",font=body_font,bg="#FFE9E3").grid(row=11,column=1,sticky='nw')
    Label(new_root,text="  * Wait until it prompts 'Result file generation is completed'.",font=body_font,bg="#FFE9E3").grid(row=12,column=1,sticky='nw')
    Label(new_root,text="  * The GPA file will be created in browsed location, and on clicking 'OK' calculator will close.",font=body_font,bg="#FFE9E3").grid(row=13,column=1,sticky='nw')
    Label(new_root,text="2) For 'Revaluation/Supplementary':",font=spl_body_font,bg="#FFE9E3").grid(row=14,column=1,sticky='nw')
    Label(new_root,text="  * Upload the Revaluation/Supplementary result PDF provided by the university.",font=body_font,bg="#FFE9E3").grid(row=15,column=1,sticky='nw')
    Label(new_root,text="  * Upload the regular GPA file updated earlier.",font=body_font,bg="#FFE9E3").grid(row=16,column=1,sticky='nw')
    Label(new_root,text="  * Click on submit and wait until it prompts 'Result file generation is completed'.",font=body_font,bg="#FFE9E3").grid(row=17,column=1,sticky='nw')
    Label(new_root,text="  * On getting the prompt changes will be done to the GPA file.",font=body_font,bg="#FFE9E3").grid(row=18,column=1,sticky='nw')    
    Label(new_root,text="Points to Remember while Uploading Files:",font=spl_body_font,bg="#FFE9E3").grid(row=19,column=1,sticky='nw')
    Label(new_root,text="  * Ensure that the PDF file ends correctly (the line after credits should be closed), otherwise the file won't support",font=body_font,bg="#FFE9E3").grid(row=20,column=1,sticky='nw')
    Label(new_root,text="    the calculation. In such a case, convert the PDF into Excel and use it as input.",font=body_font,bg="#FFE9E3").grid(row=21,column=1,sticky='nw')
    Label(new_root,text="  * If you use an online converter for converting PDF to Excel, ensure that the given input file only contains the",font=body_font,bg="#FFE9E3").grid(row=22,column=1,sticky='nw')
    Label(new_root,text="    grades table with Htno, Subcode, etc., as column names. Remove all the other things from the excel.",font=body_font,bg="#FFE9E3").grid(row=23,column=1,sticky='nw')
    Label(new_root,text="Exploring SGPA Result File",font=head_font,bg="#FFE9E3").grid(row=24,column=1,sticky='nw')
    Label(new_root,text="The obtained result file comprises 11 sheets:",font=body_font,bg="#FFE9E3").grid(row=25,column=1,sticky='nw')
    Label(new_root,text="  * Five sheets detail branch-wise SGPA calculations of students.",font=body_font,bg="#FFE9E3").grid(row=26,column=1,sticky='nw')
    Label(new_root,text="  * Five sheets contain statistics, including subject-wise pass percentages, class percentage, and top three of the class.",font=body_font,bg="#FFE9E3").grid(row=27,column=1,sticky='nw')
    Label(new_root,text="  * The last sheet ('Updated Files') provides paths of the regular file, as well as the revaluation and supplementary",font=body_font,bg="#FFE9E3").grid(row=28,column=1,sticky='nw')
    Label(new_root,text="    files updated till then on the first created regular GPA file.",font=body_font,bg="#FFE9E3").grid(row=29,column=1,sticky='nw')    
    Label(new_root,text="Calculating CGPA",font=head_font,bg="#FFE9E3").grid(row=30,column=1,sticky='nw')
    Label(new_root,text="  * To calculate the CGPA of the class, choose the 'CGPA' option.",font=body_font,bg="#FFE9E3").grid(row=31,column=1,sticky='nw')
    Label(new_root,text="  * Click on the checkboxes corresponding to the desired semesters. This will prompt you to provide the individually",font=body_font,bg="#FFE9E3").grid(row=32,column=1,sticky='nw')
    Label(new_root,text="    calculated semester-wise GPA files.",font=body_font,bg="#FFE9E3").grid(row=33,column=1,sticky='nw')
    Label(new_root,text="  * Upload the semester-wise GPA files for the selected semesters.",font=body_font,bg="#FFE9E3").grid(row=34,column=1,sticky='nw')
    Label(new_root,text="  * Browse to select the location where you want to save the output file containing the calculated CGPA results.",font=body_font,bg="#FFE9E3").grid(row=35,column=1,sticky='nw')
    Label(new_root,text="  * Wait until it prompts 'Result file generation is completed'.",font=body_font,bg="#FFE9E3").grid(row=36,column=1,sticky='nw')
    Label(new_root,text="  * The CGPA file will be created in browsed location, and on clicking 'OK' calculator will close.",font=body_font,bg="#FFE9E3").grid(row=37,column=1,sticky='nw')
    Label(new_root,text="Exploring CGPA Result File",font=head_font,bg="#FFE9E3").grid(row=38,column=1,sticky='nw')
    Label(new_root,text="The obtained result file comprises 5 sheets:",font=body_font,bg="#FFE9E3").grid(row=39,column=1,sticky='nw')
    Label(new_root,text="  * Each sheet details branch-wise CGPA calculations of students.",font=body_font,bg="#FFE9E3").grid(row=40,column=1,sticky='nw')
    """my_canvas.create_text(170,30,text="Selection of Calculation Mode:",font=head_font)
    my_canvas.create_text(220,60,text="* Determine the type of result you want to calculate.",font=body_font)
    my_canvas.create_text(461,85,text="* If you want to calculate the total GPA of a class for a semester, select 'SGPA' (Semester Grade Point Average).",font=body_font)
    my_canvas.create_text(513,110,text="* If you want to calculate the combined GPA of the cumulative semesters of the class, select 'CGPA'(Cumulative Grade Point).",font=body_font)
    my_canvas.create_text(110,140,text="SGPA Calculation:",font=head_font)
    my_canvas.create_text(110,170,text="* If SGPA is selected:",font=body_font)
    my_canvas.create_text(110,170,text="* If SGPA is selected:",font=body_font)
    my_canvas.create_text(229,195,text="a. To calculate regular results, select 'Regular':",font=body_font)
    my_canvas.create_text(229,195,text="a. To calculate regular results, select 'Regular':",font=body_font)
    my_canvas.create_text(281,220,text="b. Upload the regular result PDF provided by the university.",font=body_font)
    my_canvas.create_text(297,245,text="c. Click on the 'Submit' button to initiate the calculation process.",font=body_font)
    my_canvas.create_text(325,270,text="d. Browse the location where you want to save the calculated GPA file.",font=body_font)
    my_canvas.create_text(446,295,text="e. Upon completion of file creation, a pop-up will be generated, confirming the successful calculation.",font=body_font)
    my_canvas.create_text(463,320,text="f. To update regular results with supplementary or revaluation results, select 'Revaluation/Supplementary':",font=body_font)
    my_canvas.create_text(463,320,text="f. To update regular results with supplementary or revaluation results, select 'Revaluation/Supplementary':",font=body_font)
    my_canvas.create_text(361,345,text="g. Upload the Revaluation/Supplementary result PDF provided by the university.",font=body_font)
    my_canvas.create_text(311,370,text="h. Along with that, upload the regular GPA file obtained previously.",font=body_font)
    my_canvas.create_text(494,395,text="i. After uploading the result PDF and regular GPA file, browse the location where you want to save the output file.",font=body_font)
    my_canvas.create_text(517,420,text="j. If the supplementary exams result is present in the regular file of the next batch, directly upload the file like the normal ",font=body_font)
    my_canvas.create_text(292,440,text="supplementary file, but select 'Revaluation/Supplementary'.",font=body_font)
    my_canvas.create_text(202,465,text="* Points to Remember while Uploading Files:",font=body_font)
    my_canvas.create_text(508,490,text="a. Ensure that the PDF file ends correctly (the line after credits should be closed), otherwise the file won't support the ",font=body_font)
    my_canvas.create_text(348,515,text="calculation. In such a case, convert the PDF into Excel and use it as input.",font=body_font)
    my_canvas.create_text(525,540,text="b. If you use an online converter for converting PDF to Excel, ensure that the given input file only contains the grades table ",font=body_font)
    my_canvas.create_text(232,565,text="with Htno, Subcode, etc., as column names.",font=body_font)
    my_canvas.create_text(110,595,text="CGPA Calculation:",font=head_font)
    my_canvas.create_text(110,620,text="* If CGPA is selected:",font=body_font)
    my_canvas.create_text(110,620,text="* If CGPA is selected:",font=body_font)
    my_canvas.create_text(508,645,text="a. Click on the checkboxes corresponding to the semesters for which you have calculated individual GPA files. This ",font=body_font)
    my_canvas.create_text(348,665,text="selection helps in obtaining the cumulative GPA for the entire program.",font=body_font)
    my_canvas.create_text(437,690,text="b. For each selected semester checkbox, upload the respective calculated semester-wise GPA file.",font=body_font)
    my_canvas.create_text(305,715,text="c. These files contain the GPA data for each individual semester.",font=body_font)
    my_canvas.create_text(472,740,text="d. After uploading the semester-wise GPA files, browse the location where you want to save the output file.",font=body_font)
    my_canvas.create_text(305,765,text="e. The output file will include the calculated CGPA for the class.",font=body_font)"""
    user.mainloop()