import mysql.connector 
import tkinter as tk
from tkinter import *

class School:

    def __init__(self):
        self.Connection=False
        self.Welcome=False
        self.enter1=False
        self.enter2=False
        self.enter3=False
        self.enter4=False
        self.enter5=False
        self.enter6=False
        self.enter7=False
        self.myconnect = mysql.connector.connect(host= "localhost",user="root",password="",database="StudentMarks")

        
        self.Connection = self.myconnect


######################################################################################

    def MainWindow(self):

        MWelcome = self.Welcome

        MWelcome = tk.Tk()
        MWelcome.title("Welcome Window")
        MWelcome.geometry("660x550")

        Button1 = Button(MWelcome,text="Show Data",command=self.ShowData)
        Button1.pack(padx=20,pady=20)

        Button4 = Button(MWelcome,text="Search Studeent Id" ,command=self.SearchId)
        Button4.pack(padx=40,pady=20)

        Button5 = Button(MWelcome,text="Add Student Marks" ,command=self.AddStudentMarks)
        Button5.pack(padx=40,pady=20)

        Button2 = Button(MWelcome,text="Students More than 60%" ,command=self.TopperStudent)
        Button2.pack(padx=40,pady=20)

        Button3 = Button(MWelcome,text="Add Student" ,command=self.AddStudent)
        Button3.pack(padx=40,pady=20)


        MWelcome.mainloop()    


######################################################################################

    def ShowData(self):
        ResultW = tk.Tk()

        ResultW.title("Students Info")
        ResultW.geometry("960x350")


        myconnect = mysql.connector.connect(host= "localhost",user="root",password="",database="StudentMarks")

        mycon = myconnect.cursor()
        self.Connection = mycon

        mycon.execute("select * from StudentInfo")

        i=0

        for Student in mycon:
            for j in range(len(Student)):
                e= Entry(ResultW,width=15,fg='blue')
                e.grid(row=i,column=j)
                e.insert(END,Student[j])
            i=i+1

           

##############################################################################################################################

    def AddStudentMarks(self):
        
        def Submit():

            id = enter1.get()
            math = int(enter2.get())
            science =int(enter3.get())
            history = int(enter4.get())

            percentage = math+science+history
            percentage = percentage/3
            mycon= self.myconnect.cursor()
            mycon.execute("insert into StudentMark (StId,Mathematics,Science,History,Percentage) values ('{}','{}','{}','{}','{}')".format(id,math,science,history,percentage))
            self.Connection.commit()


        Welcome = tk.Tk()
        Welcome.title("Add New Student Marks")
        Welcome.geometry("660x550")

        Label(Welcome, text="Student ID").pack()
        enter1 = Entry(Welcome,width = 50)
        enter1.focus_set()
        enter1.pack()

        Label(Welcome, text="Mathematics").pack()
        enter2 = Entry(Welcome,width = 50)
        enter2.focus_set()
        enter2.pack()
        
        Label(Welcome, text="Science").pack()
        enter3 = Entry(Welcome,width = 50)
        enter3.focus_set()
        enter3.pack()

        Label(Welcome, text="History").pack()
        enter4 = Entry(Welcome,width = 50)
        enter4.focus_set()
        enter4.pack()

        Button3 = Button(Welcome,text="Submit" ,command=Submit)
        Button3.pack()

        

            

####################################################################################

    def SearchId(self):
        
        def Search():
            
            ResultW1 = tk.Tk()

            ResultW1.title("Search Students Info")
            ResultW1.geometry("960x350") 
            mycon = self.myconnect.cursor()
            mycon.execute("select * from StudentInfo where FName = '{}' and LName = '{}' and Grade = '{}'".format(fName.get(),lName.get(),Grade.get()))
            i=0

            myresult = mycon.fetchall()

            for Student in myresult:
                for j in range(len(Student)):
                    e= Entry(ResultW1,width=15,fg='blue')
                    e.grid(row=i,column=j)
                    e.insert(END,Student[j])
            i=i+1
                
            
            

        ResultW = tk.Tk()

        ResultW.title("Search Students Info")
        ResultW.geometry("960x350")   
    
        

        Label(ResultW, text="First Name").pack()
        fName = Entry(ResultW,width = 50)
        fName.focus_set()
        fName.pack()

        Label(ResultW, text="Last Name").pack()
        lName = Entry(ResultW,width = 50)
        lName.focus_set()
        lName.pack()

        Label(ResultW, text="Grade").pack()
        Grade = Entry(ResultW,width = 50)
        Grade.focus_set()
        Grade.pack()

        Button1 = Button(ResultW,text="Search" ,command=Search)
        Button1.pack()

        


######################################################################################

    def TopperStudent(self):

        ResultW = tk.Tk()

        ResultW.title("Topper Students")
        ResultW.geometry("960x350")


        myconnect = mysql.connector.connect(host= "localhost",user="root",password="",database="StudentMarks")

        mycon = myconnect.cursor()

        mycon.execute("SELECT s.StId, s.FName, s.LName FROM StudentInfo s INNER JOIN StudentMark sm ON s.StId = sm.StId WHERE sm.Percentage > 60")

        i=0

        for Student in mycon:
            for j in range(len(Student)):
                e= Entry(ResultW,width=15,fg='blue')
                e.grid(row=i,column=j)
                e.insert(END,Student[j])
            i=i+1



######################################################################################

    def AddStudent(self):

        Welcome = tk.Tk()
        Welcome.title("Add New Student Info")
        Welcome.geometry("660x550")

        Label(Welcome, text="First Name").pack()
        self.enter1 = Entry(Welcome,width = 50)
        self.enter1.focus_set()
        self.enter1.pack()

        Label(Welcome, text="Last Name").pack()
        self.enter2 = Entry(Welcome,width = 50)
        self.enter2.focus_set()
        self.enter2.pack()
        
        Label(Welcome, text="Grade").pack()
        self.enter7 = Entry(Welcome,width = 50)
        self.enter7.focus_set()
        self.enter7.pack()
        
        
        Label(Welcome, text="Birth Date(dd/mm/yy)").pack()
        self.enter3 = Entry(Welcome,width = 50)
        self.enter3.focus_set()
        self.enter3.pack()

        Label(Welcome, text="Parent Name").pack()
        self.enter4 = Entry(Welcome,width = 50)
        self.enter4.focus_set()
        self.enter4.pack()

        Label(Welcome, text="City").pack()
        self.enter5 = Entry(Welcome,width = 50)
        self.enter5.focus_set()
        self.enter5.pack()

        Label(Welcome, text="Phone").pack()
        self.enter6 = Entry(Welcome,width = 50)
        self.enter6.pack()
        self.enter6.focus_set()

        Submit = Button(Welcome,text="Submit!",command=self.AddData)
        Submit.pack()

######################################################################################        
            
    def AddData(self):
        fName = self.enter1.get()
        lName = self.enter2.get()
        birthD = self.enter3.get()
        pName = self.enter4.get()
        cName = self.enter5.get()
        PNo = self.enter6.get()
        Grade = self.enter7.get()

        myconnect = mysql.connector.connect(host= "localhost",user="root",password="",database="StudentMarks")

        mycon = myconnect.cursor()

         

        
        mycon.execute("insert into StudentInfo(FName,LName,Grade,BirthDate,PName,City,Phone) values('{}','{}','{}','{}','{}','{}','{}')".format(fName,lName,Grade,birthD,pName,cName,PNo))
        myconnect.commit()

        self.enter1.delete(0,END)
        self.enter2.delete(0,END)
        self.enter3.delete(0,END)
        self.enter4.delete(0,END)
        self.enter5.delete(0,END)
        self.enter6.delete(0,END)
        self.enter7.delete(0,END)

        self.ShowData()


######################################################################################
######################################################################################        


def main():
    
    obj = School()

    obj.MainWindow()


if __name__ == "__main__":
    main()    