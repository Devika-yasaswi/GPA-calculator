from tkinter import *
def user_guide():
    user=Tk()
    user.geometry("1050x700+300+0")
    #user.configure(bg="#1E90FF")
    user.title("CGPA/SGPA Calculator")
    img=PhotoImage(file="Background.png")
    my_canvas=Canvas(user,width=1025,height=620)
    my_canvas.pack(fill='both',expand=True)
    my_canvas.create_image(0,0,image=img,anchor="nw")
    my_canvas.pack(side=LEFT,fill=Y,expand=1)

    my_scrollbar=Scrollbar(user,orient=VERTICAL,command=my_canvas.yview)

    my_scrollbar.pack(side=RIGHT,fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)

    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    head_font=('Times new Roman',18,'bold',"italic")   #Font style for headings
    body_font=('Times new Roman',15)
    #spl_body_font=('Times new Roman',15,'bold')
    my_canvas.create_text(170,30,text="Selection of Calculation Mode:",font=head_font)
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
    my_canvas.create_text(305,765,text="e. The output file will include the calculated CGPA for the class.",font=body_font)
    user.mainloop()