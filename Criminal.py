from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
    
class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1490x750+0+0')
        self.root.title('CRIME MANAGEMENT SYSTEM')

        self.var_caseid=StringVar()
        self.var_criminalno=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arretdate=StringVar()
        self.var_crimedate=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthmark=StringVar()
        self.var_crimetype=StringVar()
        self.var_fathername=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()


        lbl_title = Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM',font=('times new roman',30,'bold'),bg ='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1490,height=60)

        img_logo=Image.open('images/ncrlogo.png')
        img_logo=img_logo.resize((60,60),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=80,y=5,width=60,height=60)

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=60,width=1530,height=130)

        img1=Image.open('images\police1.jpg')
        img1=img1.resize((540,160),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        img2=Image.open('images/police 2.jpg')
        img2=img2.resize((540,160),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=500,y=0,width=490,height=160)

        img3=Image.open('images\police 3.jpeg')
        img3=img3.resize((540,160),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=990,y=0,width=480,height=160)

        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=190,width=1320,height=490)

        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='CRIMINAL INFORMATION',font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=5,width=1280,height=240)

        caseid = Label(upper_frame,text='Case ID:',font=('arial',11,'bold'),bg= 'white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry = ttk.Entry(upper_frame,textvariable=self.var_caseid ,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1, padx=2,sticky=W)

        lbl_criminal_no = Label(upper_frame,text='Criminal No.:',font=('arial',11,'bold'),bg= 'white')
        lbl_criminal_no.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_criminal_no = ttk.Entry(upper_frame,textvariable=self.var_criminalno,width=22,font=('arial',11,'bold'))
        txt_criminal_no.grid(row=0,column=3, padx=2,pady=7)

        lbl_criminal_name = Label(upper_frame,text='Name:',font=('arial',11,'bold'),bg= 'white')
        lbl_criminal_name.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_criminal_name = ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_criminal_name.grid(row=1,column=1, padx=2,pady=7)

        lbl_criminal_nickname = Label(upper_frame,text='NickName:',font=('arial',11,'bold'),bg= 'white')
        lbl_criminal_nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_criminal_nickname = ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('arial',11,'bold'))
        txt_criminal_nickname.grid(row=1,column=3, padx=2,pady=7)

        lbl_criminal_arrestdate = Label(upper_frame,text='Arrest Date:',font=('arial',11,'bold'),bg= 'white')
        lbl_criminal_arrestdate.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_criminal_arrestdate = ttk.Entry(upper_frame,textvariable=self.var_arretdate,width=22,font=('arial',11,'bold'))
        txt_criminal_arrestdate.grid(row=2,column=1, padx=2,pady=7)

        lbl_criminal_crimedate = Label(upper_frame,text='Crime Date:',font=('arial',11,'bold'),bg= 'white')
        lbl_criminal_crimedate.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_criminal_crimedate = ttk.Entry(upper_frame,textvariable=self.var_crimedate,width=22,font=('arial',11,'bold'))
        txt_criminal_crimedate.grid(row=2,column=3, padx=2,pady=7)

        lbl_criminal_address = Label(upper_frame,text='Address:',font=('arial',11,'bold'),bg= 'white')
        lbl_criminal_address.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_criminal_address = ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_criminal_address.grid(row=3,column=1, padx=2,pady=7)

        lbl_criminal_age = Label(upper_frame,text='Age:',font=('arial',11,'bold'),bg= 'white')
        lbl_criminal_age.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_criminal_age = ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold'))
        txt_criminal_age.grid(row=3,column=3, padx=2,pady=7)

        lbl_criminal_occupation = Label(upper_frame,text='Occupation:',font=('arial',11,'bold'),bg= 'white')
        lbl_criminal_occupation.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_criminal_occupation = ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('arial',11,'bold'))
        txt_criminal_occupation.grid(row=4,column=1, padx=2,pady=7)

        lbl_criminal_birthmark = Label(upper_frame,text='BirthMark:',font=('arial',11,'bold'),bg= 'white')
        lbl_criminal_birthmark.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_criminal_birthmark = ttk.Entry(upper_frame,textvariable=self.var_birthmark,width=22,font=('arial',11,'bold'))
        txt_criminal_birthmark.grid(row=4,column=3, padx=2,pady=7)

        lbl_crimetype = Label(upper_frame,text='Crime Type:',font=('arial',11,'bold'),bg= 'white')
        lbl_crimetype.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_crimetype = ttk.Entry(upper_frame,textvariable=self.var_crimetype,width=22,font=('arial',11,'bold'))
        txt_crimetype.grid(row=0,column=5, padx=2,pady=7)

        lbl_criminal_fathername = Label(upper_frame,text='Father Name:',font=('arial',11,'bold'),bg= 'white')
        lbl_criminal_fathername.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_criminal_fathername = ttk.Entry(upper_frame,textvariable=self.var_fathername,width=22,font=('arial',11,'bold'))
        txt_criminal_fathername.grid(row=1,column=5, padx=2,pady=7)

        lbl_criminal_gender = Label(upper_frame,text='Gender:',font=('arial',11,'bold'),bg= 'white')
        lbl_criminal_gender.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        lbl_criminal_wanted = Label(upper_frame,text='Most Wanted:',font=('arial',11,'bold'),bg= 'white')
        lbl_criminal_wanted.grid(row=3,column=4,sticky=W,padx=2,pady=7)

        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=675,y=83,width=190,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',9,'bold'),bg= 'white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)

        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',9,'bold'),bg= 'white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=675,y=125,width=190,height=30)

        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=('arial',9,'bold'),bg= 'white')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)

        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',9,'bold'),bg= 'white')
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=190,width=400,height=25)

        btn_add=Button(button_frame,command=self.add_data,text='Record Save',font=('arial',9,'bold'),width=12,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=4,pady=2)

        btn_update=Button(button_frame,command=self.update_data,text='Update',font=('arial',9,'bold'),width=12,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=4,pady=2)

        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=('arial',9,'bold'),width=12,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=4,pady=2)

        btn_clear=Button(button_frame,command=self.clear_data,text='Clear',font=('arial',9,'bold'),width=12,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=4,pady=2)

        img_crime=Image.open('images\police 3.jpeg')
        img_crime=img_crime.resize((370,200),Image.Resampling.LANCZOS)
        self.photo_crime=ImageTk.PhotoImage(img_crime)

        self.img_criminal=Label(upper_frame,image=self.photo_crime)
        self.img_criminal.place(x=900,y=0,width=370,height=200)

        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='CRIMINAL INFORMATION Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=250,width=1280,height=230)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Criminal Data',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1270,height=60)

        search_by = Label(search_frame,text='Search By:',font=('arial',11,'bold'),fg= 'white',bg='red')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        self.var_com_search=StringVar()
        combo_search=ttk.Combobox(search_frame,font=('arial',11,'bold'),textvariable=self.var_com_search,width=18,state='readonly')
        combo_search['value']=('Select Option','case_id','criminal_no')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        search_txt= ttk.Entry(search_frame,width=18,textvariable=self.var_search,font=('arial',11,'bold'))
        search_txt.grid(row=0,column=2,sticky=W,padx=5) 

        btn_search=Button(search_frame,command=self.search_data,text='Search',font=('arial',9,'bold'),width=12,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,sticky=W,padx=5)

        btn_showall=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',9,'bold'),width=12,bg='blue',fg='white')
        btn_showall.grid(row=0,column=4,sticky=W,padx=5)

        crime_agency = Label(search_frame,text='NATIONAL CRIME AGENCY',font=('arial',30,'bold'),bg= 'white',fg='crimson')
        crime_agency.grid(row=0,column=5,sticky=W,padx=50,pady=0)

        table_frame = Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1270,height=140)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2',text='Crime No')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='Nick Name')
        self.criminal_table.heading('5',text='Arrest Date')
        self.criminal_table.heading('6',text='Crime of Date')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')

        self.criminal_table['show']='headings'
        self.criminal_table.column('1',width=80)
        self.criminal_table.column('2',width=80)
        self.criminal_table.column('3',width=80)
        self.criminal_table.column('4',width=80)
        self.criminal_table.column('5',width=80)
        self.criminal_table.column('6',width=80)
        self.criminal_table.column('7',width=80)
        self.criminal_table.column('8',width=80)
        self.criminal_table.column('9',width=80)
        self.criminal_table.column('10',width=80)
        self.criminal_table.column('11',width=80)
        self.criminal_table.column('12',width=80)
        self.criminal_table.column('13',width=80)
        self.criminal_table.column('14',width=80)

        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    def add_data(self):
        if self.var_caseid.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='ravi1980',database='criminalmanagement')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into new_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                            self.var_caseid.get(),
                                                                                                            self.var_criminalno.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_nickname.get(),
                                                                                                            self.var_arretdate.get(),
                                                                                                            self.var_crimedate.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_age.get(),
                                                                                                            self.var_occupation.get(),
                                                                                                            self.var_birthmark.get(),
                                                                                                            self.var_crimetype.get(),
                                                                                                            self.var_fathername.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_wanted.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal Record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='ravi1980',database='criminalmanagement')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from new_table')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursur_row = self.criminal_table.focus()
        content=self.criminal_table.item(cursur_row)
        data=content['values']
        self.var_caseid.set(data[0])
        self.var_criminalno.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3]),
        self.var_arretdate.set(data[4])
        self.var_crimedate.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthmark.set(data[9]),
        self.var_crimetype.set(data[10])
        self.var_fathername.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])

    def update_data(self):
        if self.var_caseid.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to update this criminal record?')
                if update>0:
                     conn=mysql.connector.connect(host='localhost',username='root',password='ravi1980',database='criminalmanagement')
                     my_cursor=conn.cursor()
                     my_cursor.execute('update new_table set criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,date0fcrime=%s,address=%s,age=%s,occupation=%s,birthmark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where case_id=%s',(
                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                       self.var_criminalno.get(),
                                                                                                                                                                                                                                                       self.var_name.get(),
                                                                                                                                                                                                                                                       self.var_nickname.get(),
                                                                                                                                                                                                                                                       self.var_arretdate.get(),
                                                                                                                                                                                                                                                       self.var_crimedate.get(),
                                                                                                                                                                                                                                                       self.var_address.get(),
                                                                                                                                                                                                                                                       self.var_age.get(),
                                                                                                                                                                                                                                                       self.var_occupation.get(),
                                                                                                                                                                                                                                                       self.var_birthmark.get(),
                                                                                                                                                                                                                                                       self.var_crimetype.get(),
                                                                                                                                                                                                                                                       self.var_fathername.get(),
                                                                                                                                                                                                                                                       self.var_gender.get(),
                                                                                                                                                                                                                                                       self.var_wanted.get(),
                                                                                                                                                                                                                                                       self.var_caseid.get()
                                                                                                                                                                                                                                                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal Record has been Updated')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')
    
    def delete_data(self):
        if self.var_caseid.get()=="":
            messagebox.showerror('Error','All fields are required')
        
        else:
            try:
                delete=messagebox.askyesno('Delete','Are you sure to delete this criminal record?')
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='ravi1980',database='criminalmanagement')
                    my_cursor=conn.cursor()
                    sql = 'delete from new_table where case_id=%s'
                    value=(self.var_caseid.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal Record has been Successfully deleted')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    def clear_data(self):
        self.var_caseid.set("")
        self.var_criminalno.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arretdate.set("")
        self.var_crimedate.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_crimetype.set("")
        self.var_fathername.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All fields are required')
        
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='ravi1980',database='criminalmanagement')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from new_table where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')
                 








if __name__ == '__main__':
    root = Tk()
    obj=Criminal(root)
    root.mainloop()