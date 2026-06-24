import csv
import tkinter as tk
from tkinter import messagebox

def save_tasks():
    with open("task_list.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for i in range(l2.size()):
            writer.writerow([l2.get(i)])

def add():
    e1 = e.get().strip()

    if e1 != "":

        for i in range(l2.size()):
            if l2.get(i).lower() == e1.lower():
                l1.configure(text="Task already exists", fg="red")
                e.delete(0, tk.END)
                return

        l1.configure(text="Task added", fg="green")
        l2.insert(tk.END, e1)
        update_count()
        save_tasks()
        l4.configure(text="Data Saved Successfully", fg="green")

    else:
        l1.configure(text="Please enter a task", fg="red")

    e.delete(0, tk.END)

def Delete_task():
    selected = l2.curselection()

    if selected:
        l2.delete(selected[0])
        update_count()
        save_tasks()
        l3.configure(text="Task Deleted", fg="blue")
    else:
        l3.configure(text="Please select task", fg="red")
def update_count():
    c=l2.size()
    l5.configure(text=f"Total Tasks: {c}", fg="blue")
    

    
def load():
    try:
        with open("task_list.csv","r")as file:
            reader = csv.reader(file)
            for row in reader:
                l2.insert(tk.END, row[0])
            update_count()
    except FileNotFoundError:
        pass

def clear_all():
    confirm = messagebox.askyesno(
        "Confirm",
        "Delete all tasks?"
    )

    if confirm:
        l2.delete(0, tk.END)
        save_tasks()
        update_count()
        l6.configure(text="All tasks deleted", fg="green")

def edit_task():
    selected = l2.curselection()

    if selected:
        index = selected[0]
        new_task = e.get().strip()

        if new_task != "":
            l2.delete(index)
            l2.insert(index, new_task)
            save_tasks()
            update_count()
            l3.configure(text="Task Updated", fg="green")
            e.delete(0, tk.END)

        else:
            l3.configure(text="Enter new task", fg="red")

    else:
        l3.configure(text="Please select task", fg="red")

def search_task():
    keyword = s.get().strip()

    if keyword == "":
        show_all()
        return

    l2.delete(0, tk.END)

    found = False

    with open("task_list.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if keyword.lower() in row[0].lower():
                l2.insert(tk.END, row[0])
                found = True

    if not found:
        l3.configure(text="Task Not Found", fg="red")
    else:
        l3.configure(text="Task Found", fg="green")

    update_count()

    update_count()
    
def show_all():
    l2.delete(0, tk.END)
    load()
    s.delete(0, tk.END)



    
root=tk.Tk()
root.geometry("600x500")
root.title("TO DO LIST APPLICATION")
l=tk.Label(root,text="Enter task to do",fg="red")
l.grid(row=1,column=0,padx=10,pady=20)
e=tk.Entry(root,width=30)
e.grid(row=1,column=1,padx=10,pady=20)
l1=tk.Label(root,text=" ")
l1.grid(row=2,column=1,padx=20)
b=tk.Button(root,text="Add",command=add).grid(row=2,column=0,padx=30)

scroll=tk.Scrollbar(root)

l2=tk.Listbox(root,width=40,height=8,yscrollcommand=scroll.set)
l2.grid(row=3,column=0,columnspan=2,padx=10,pady=20)

scroll.grid(row=3,column=2,sticky="ns")

scroll.config(command=l2.yview)

b1=tk.Button(root,text="Delete task",command=Delete_task).grid(row=4,column=0,padx=10)
l3=tk.Label(root,text="")
l3.grid(row=4,column=1,padx=10)

l4=tk.Label(root,text="")
l4.grid(row=5,column=1,padx=10)
l5=tk.Label(root,text="")
l5.grid(row=5,column=2,padx=10)
load()
b2=tk.Button(root,text="Clear All",command=clear_all).grid(row=6,column=0,padx=10)
l6=tk.Label(root,text="")
l6.grid(row=6,column=1,padx=10)
b3=tk.Button(root,text="Edit Task",command=edit_task)
b3.grid(row=7,column=1,padx=10)
l7=tk.Label(root,text="Search Task:",fg="red")
l7.grid(row=8,column=0,padx=10,pady=20)
s=tk.Entry(root,width=30)
s.grid(row=8,column=1,padx=10,pady=20)
b4=tk.Button(root,text="Search",command=search_task)
b4.grid(row=9,column=0,padx=10)
b5=tk.Button(root,text="Show All",command=show_all)
b5.grid(row=9,column=1,padx=10)
root.bind("<Return>", lambda event: add())

root.mainloop()