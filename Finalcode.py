"""This code belongs to sudip shrestha .:!:."""
from tkinter import *
import mysql.connector
from tkinter import ttk,messagebox

try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='darknights',
        database='assign',
        port=3308
    )
    cur = con.cursor()

    # if con!=None:
    #     print('connected')
except mysql.connector.Error as e:
    print(e)


class assignment:

    def add_info(self):
        try:
            lab1 = self.entryid.get()
            lab2 = self.entryFname.get()
            lab3 = self.entrylname.get()
            lab4 = self.entrydeg.get()
            lab5 = self.entryadd.get()
            lab6 = self.entryage.get()
            lab7 = self.entrynum.get()
            lab8 = self.gender.get()
            if not lab1 or not lab2 or not lab3 or not lab4 or not lab5 or not lab6 or not lab7 or not lab8:
                messagebox.showinfo('Info', 'Fill all the entry boxes')
                return


            if lab2.isdigit():
                messagebox.showinfo("Info", "Invalid First Name")
                return

            elif lab3.isdigit():
                messagebox.showinfo("Info", "Invalid Last Name")
                return


            elif lab5.isdigit():
                messagebox.showinfo("Info", "Invalid Address")
                return

            elif not lab1.isdigit():
                messagebox.showinfo("Info", "Invalid Id.Enter number only.")
                return

            elif not lab6.isdigit():
                messagebox.showinfo("Info", "Invalid Age.Enter number only")
                return

            elif not lab7.isdigit():
                messagebox.showinfo("Info", "Invalid Phone number.Enter number only.")
                return

            elif len(lab7) <= 9:
                messagebox.showinfo("Info", "Phone number is not long enough.")
                return
            query = ' insert into btable values(%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (lab1, lab2, lab3, lab6, lab8, lab4, lab5,lab7)
            cur.execute(query, values)
            print('1 row inserted')
            con.commit()
            self.clear()
            self.show()
        except mysql.connector.IntegrityError as error:
            if str(error)[0:4] == '1062':
                messagebox.showinfo("Info","Duplicate Id entry found")




    def show(self):
        query = 'select * from btable'
        cur.execute(query)
        rows = cur.fetchall()

        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('', END, values=row)

    def clear(self):
        self.entryid.delete(0, END)
        self.entryFname.delete(0, END)
        self.entrylname.delete(0, END)
        self.entrydeg.delete(0, END)
        self.entryadd.delete(0, END)
        self.entryage.delete(0, END)
        self.entrynum.delete(0, END)
        self.gender.delete(0,END)


    def update(self):
        try:
            lab1 = self.entryid.get()
            lab2 = self.entryFname.get()
            lab3 = self.entrylname.get()
            lab4 = self.entrydeg.get()
            lab5 = self.entryadd.get()
            lab6 = self.entryage.get()
            lab7 = self.entrynum.get()
            lab8= self.gender.get()
            if not lab1 or not lab2 or not lab3 or not lab4 or not lab5 or not lab6 or not lab7 or not lab8:
                messagebox.showinfo('Info', 'Fill all the entry boxes')
                return

            if lab2.isdigit():
                messagebox.showinfo("Info", "Invalid First Name")
                return

            elif lab3.isdigit():
                messagebox.showinfo("Info", "Invalid Last Name")
                return

            elif lab4.isdigit():
                messagebox.showinfo("Info", "Invalid Degree")
                return

            elif lab5.isdigit():
                messagebox.showinfo("Info", "Invalid Address")
                return

            elif not lab1.isdigit():
                messagebox.showinfo("Info", "Invalid Id.Enter number only.")
                return

            elif not lab6.isdigit():
                messagebox.showinfo("Info", "Invalid Age.Enter number only")
                return

            elif not lab7.isdigit():
                messagebox.showinfo("Info", "Invalid Phone number.Enter number only.")
                return

            elif len(lab7) <= 9:
                messagebox.showinfo("Info", "Phone number is not long enough.")
                return


            query = ' update btable set  fname=%s, lname=%s, Degree=%s, address=%s, age=%s, numb=%s, gender=%s where id=%s'
            values = (lab2, lab3, lab4, lab5, lab6, lab7,lab8, lab1)
            cur.execute(query, values)
            con.commit()
            self.clear()
            self.show()
        except ValueError:
            messagebox.showinfo("Info", "please fill all the boxes.")

    def pointer(self,event):
        try:
            point = self.student_table.focus()
            content = self.student_table.item(point)
            row = content['values']
            #   print(row)
            self.clear()
            if len(row) != 0:
                self.entryid.insert(0, row[0])
                self.entryFname.insert(0, row[1])
                self.entrylname.insert(0, row[2])
                self.entryage.insert(0, row[3])
                self.gender.insert(0,row[4])
                self.entrydeg.insert(0, row[5])
                self.entryadd.insert(0, row[6])
                self.entrynum.insert(0, row[7])
        except IndexError:
            pass

    def delete(self):
        try:
            selected_item = self.student_table.selection()
            self.student_table.delete(selected_item)

            query = 'delete from btable where id=%s'
            id = self.entryid.get()
            values = (id,)
            cur.execute(query, values)
            con.commit()
            self.clear()
        except:
            messagebox.showinfo('Info','Select data from table!')

    def refresh(self):
        self.clear()
        self.show()

    def linear_search(self, combo, find):  # combo= directory of column, find= searched data
        try:

            if self.search.get() == 'Fname':
                column = 1

            elif self.search.get() == 'lname':
                column = 2

            elif self.search.get() == 'Address':
                column = 6

            elif self.search.get() == 'Age':
                column = 3
                find = int(find)

            elif self.search.get() == 'Gender':
                column = 4

            elif self.search.get() == 'Degree':
                column = 5

            elif self.search.get() == 'ID':
                find = int(find)
                column = 0


            else:
                column = 7

            found_list = []
            for row in combo:
                if row[column] == find:
                    found_list.append(row)
            # print(found_list)
            return found_list

        except ValueError:
            messagebox.showinfo('Info', 'No valid data selected. ')

    def searching(self):
        find = self.entrysea.get()
        box = self.search.get()
        if not box:
            messagebox.showinfo('Info', 'No valid data found.Choose from option')
        elif not find:
            messagebox.showinfo('Info', 'No value inserted.')
        else:
            query1 = " select * from btable "
            cur.execute(query1)
            table = cur.fetchall()
            # print(table)
            rows = self.linear_search(table, find)

            print(rows)
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())

            for row in rows:
                self.student_table.insert('', END, values=row)

            if not rows:
                messagebox.showinfo("Info", 'No data found in the database.')

            self.clear()

    def partition(self, table, start, end):
        if not self.sort_by.get():
            messagebox.showinfo('Info', 'No valid data found. Choose from option')
            return
        else:
            if self.sort_by.get() == 'ID':
                column = 0

            elif self.sort_by.get() == 'Fname':
                column = 1

            elif self.sort_by.get() == 'lname':
                column = 2

            elif self.sort_by.get() == 'Age':
                column = 3

            elif self.sort_by.get() == 'Gender':
                column = 4

            elif self.sort_by.get() == 'Degree':
                column = 5

            elif self.sort_by.get() == 'Address':
                column = 6

            else:
                column = 7

            num_sort = (start - 1)
            pivot = table[end][column]
            if self.var.get():
                if self.var.get() == 'Ascending':
                    for var in range(start, end):
                        if table[var][column] <= pivot:
                            num_sort = num_sort + 1
                            table[num_sort], table[var] = table[var], table[num_sort]

                    table[num_sort + 1], table[end] = table[end], table[num_sort + 1]
                    return (num_sort + 1)
                elif self.var.get() == 'Descending':
                    for var in range(start, end):
                        if table[var][column] >= pivot:
                            num_sort = num_sort + 1
                            table[num_sort], table[var] = table[var], table[num_sort]

                    table[num_sort + 1], table[end] = table[end], table[num_sort + 1]
                    return (num_sort + 1)

            else:
                messagebox.showinfo('Info', 'Choose from radiobutton.')

    # Function to do Quick sort
    def quick_sort(self, table, start, end):
        if start < end:
            self.part = self.partition(table, start, end)
            self.quick_sort(table, start, self.part - 1)
            self.quick_sort(table, self.part + 1, end)
            return (table)
    def sorting(self):

        try:
            query = "select * from btable"
            cur.execute(query)
            table = cur.fetchall()

            self.quick_sort(table, 0, len(table) - 1)
            print()
            sortby = int()
            self.student_table.delete(*self.student_table.get_children())
            for row in table:
                self.student_table.insert("", 'end', values=row)
                con.commit()
        except:
            messagebox.showerror("info", "No value selected.")



    def __init__(self, root):
        self.root = root
        # ==============Button frame=========
        self.btn_frame = Frame(self.root, bd=4, bg='gray', relief=RIDGE)
        self.btn_frame.place(x=20, y=240, width=600, height=40)

        self.frame = Frame(self.root, bd=4, relief=RIDGE)
        self.frame.place(x=20, y=280, width=600, height=150)

        self.table_frame = Frame(self.root, bd=4, bg='gray', relief=RIDGE)
        self.table_frame.place(x=20, y=430, width=600, height=150)

        # ==================Lable==================
        self.fname = Label(self.root, text='First name',font='times 12 bold italic').grid(row=0, column=0, padx=15, pady=15)
        self.lname = Label(self.root, text='Last name',font='times 12 bold italic').grid(row=0, column=2, padx=15, pady=15)
        self.id = Label(self.root, text='ID',font='times 12 bold italic').grid(row=1, column=0, padx=15, pady=15)
        self.age = Label(self.root, text='Age',font='times 12 bold italic').grid(row=1, column=2, padx=15, pady=15)
        self.gender =Label(self.root,text='Gender',font='times 12 bold italic').grid(row=2, column=0, padx=15, pady=15)
        self.degree = Label(self.root, text='Degree',font='times 12 bold italic').grid(row=2, column=2, padx=15, pady=15)
        self.address = Label(self.root, text='Address',font='times 12 bold italic').grid(row=3, column=0, padx=15, pady=15)
        self.number = Label(self.root, text='Number',font='times 12 bold italic').grid(row=3, column=2, padx=15, pady=15)

        self.sortby = Label(self.frame, text='Sortby',font='times 12 bold italic').grid(row=0, column=0, padx=10, pady=15)
        self.searchlbl = Label(self.frame, text='Search By',font='times 12 bold italic').grid(row=0, column=3, padx=10, pady=15)
        self.searchby = Label(self.frame, text='Search Text',font='times 12 bold italic').grid(row=1, column=3, padx=10, pady=15)

        # ================entry================

        self.entryFname = Entry(self.root,bd=4,font='arial 10  italic')
        self.entryFname.grid(row=0, column=1, padx=15, pady=15)
        self.entrylname = Entry(self.root,bd=4,font='arial 10  italic')
        self.entrylname.grid(row=0, column=4, padx=15, pady=15)
        self.entryid = Entry(self.root, bd=4, font='arial 10  italic')
        self.entryid.grid(row=1, column=1, padx=15, pady=15)
        self.entryage = Entry(self.root, bd=4,font='arial 10  italic')
        self.entryage.grid(row=1, column=4, padx=15, pady=15)
        self.entryadd = Entry(self.root,bd=4,font='arial 10  italic')
        self.entryadd.grid(row=3, column=1, padx=15, pady=15)
        self.entrynum = Entry(self.root,bd=4,font='arial 10  italic')
        self.entrynum.grid(row=3, column=4, padx=15, pady=15)

        self.entrysea = Entry(self.frame,bd=4,font='arial 10  italic')
        self.entrysea.grid(row=1, column=4, padx=15, pady=15)

        #==========optionbox=========
        self.sort_by = ttk.Combobox(self.frame, font='arial 10 bold italic', state='readonly', width=20)
        self.sort_by['values'] = ('ID', 'Fname', 'lname', 'Age', 'Gender', 'Degree', 'Address', 'Number')
        self.sort_by.grid(row=0, column=1, pady=10, padx=20)

        self.search = ttk.Combobox(self.frame, font=('arial 10 bold italic'), state='readonly',width=19)
        self.search['values'] = ('ID','Fname', 'lname', 'Age','Gender','Degree', 'Address',   'Number')
        self.search.grid(row=0, column=4, pady=10, padx=20)

        self.gender = ttk.Combobox(self.root,font='arial 10  italic',width=18)
        self.gender['values'] = ('Male', 'Female', 'Others')
        self.gender.grid(row=2, column=1, pady=10, padx=10)

        self.entrydeg = ttk.Combobox(self.root, font='arial 10  italic', width=18)
        self.entrydeg['values'] = ('BSc. (Hons) Computing','BSc.(Hons) Ethical Hacking')
        self.entrydeg.grid(row=2, column=4, padx=15, pady=15)


        #=============radiobutton==========

        self.var = StringVar()
        self.desc = ttk.Radiobutton(self.frame,
                           text="Descending", variable=self.var, value="Descending")
        self.desc.grid(row=1, column=1, padx=10, pady=10)

        self.ascend = ttk.Radiobutton(self.frame,
                             text="Ascending", variable=self.var, value="Ascending")
        self.ascend.grid(row=1, column=0, padx=10, pady=10)
        # =================Buttons==============
        self.button = Button(self.btn_frame, text='Add',font='times 12 bold italic', command=self.add_info, width=10, height=1).grid(row=7,
                                                                                                         column=0,
                                                                                                         padx=25)
        self.button1 = Button(self.btn_frame, text='update',font='times 12 bold italic', command=self.update, width=10, height=1).grid(row=7,
                                                                                                           column=1,
                                                                                                           padx=25)
        self.button2 = Button(self.btn_frame, text='Delete',font='times 12 bold italic', command=self.delete, width=10, height=1).grid(row=7,
                                                                                                           column=2,
                                                                                                           padx=25)
        self.button3 = Button(self.btn_frame, text='Clear',font='times 12 bold italic', command=self.clear, width=10, height=1).grid(row=7,
                                                                                                         column=3,
                                                                                                         padx=25)

        self.button4 = Button(self.frame, text='Search', font='times 12 bold italic', command=self.searching, width=10,
                              height=1).place(x=450, y=110)
        self.button5 = Button(self.frame, text='Sort', font='times 12 bold italic', command=self.sorting, width=10,
                              height=1).place(x=50, y=110)
        self.button6 = Button(self.frame, text='Refresh', font='times 12 bold italic', command=self.refresh, width=10,
                              height=1).place(x=250, y=110)

        # =========scrollbar=======
        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        # ==============table=================
        self.student_table = ttk.Treeview(self.table_frame,
                                          column=('id', 'fname', 'lname', 'age','gender', 'deg', 'address', 'number'),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)

        self.student_table.heading('id', text='ID')
        self.student_table.heading('fname', text='Fname')
        self.student_table.heading('lname', text='lname')
        self.student_table.heading('age', text='Age')
        self.student_table.heading('gender',text='Gender')
        self.student_table.heading('deg', text='Degree')
        self.student_table.heading('address', text='Address')

        self.student_table.heading('number', text="Number")
        self.student_table['show'] = 'headings'
        self.student_table.pack()

        self.student_table.column('id', width=50)
        self.student_table.column('fname', width=80)
        self.student_table.column('lname', width=80)
        self.student_table.column('age', width=60)
        self.student_table.column('gender',width=80)
        self.student_table.column('deg', width=150)
        self.student_table.column('address', width=80)
        self.student_table.column('number', width=70)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)

        self.show()

        self.student_table.bind('<ButtonRelease-1>', self.pointer)

        self.student_table.pack(fill=BOTH, expand=True)




root = Tk()
root.title("!!!!Student register!!!!")
root.geometry('650x600')
root.resizable(0,0)
abc = assignment(root)
root.mainloop()