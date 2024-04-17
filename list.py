import tkinter as tk
from tkinter import messagebox

tasks=[]

def adds():
    task=text.get()
    if task:
        tasks.append(task)
        list.insert(tk.END, task)
        text.delete(0, tk.END)
        messagebox.showinfo("Successful", "Task added Successfully!")
    else:
        messagebox.showwarning("Warning!", "Please enter a task!")

def deletes():
    sel_index = list.curselection()
    if sel_index:
        index = sel_index[0]
        task = list.get(index)
        tasks.remove(task)
        list.delete(index)
        messagebox.showinfo("Successful", "Task deleted Successfully!")
    else:
        messagebox.showwarning("Warning!", "Please select a task to delete!")

def delete_all():
    tasks.clear()
    list.delete(0, tk.END)
    messagebox.showinfo("Successful", "All tasks deleted Successfully!")

def exit():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

root=tk.Tk()
root.title("To-Do List Application")
root.geometry("500x500")
root.configure(bg="thistle1")

label=tk.Label(root,text="My To-Do List!!",fg="blue",font=("Cambria",37,"bold"),bg="thistle1",pady=20,padx=10)
label.grid(row=0, column=0,columnspan=2,padx=58)
text=tk.Entry(root,bg="lightcyan1",width=50,bd=3,font=("Helvetica",12,"bold"))
text.grid(row=1,column=0,columnspan=2,padx=13,pady=25)
add=tk.Button(root,text="Add Task", width=15, command=adds,bg="lightcoral",fg="white",bd=4,padx=2,pady=2,font=("Helvetica",12,"bold"))
add.grid(row=2, column=0,padx=25)
delete=tk.Button(root,text="Delete Task", width=15, command=deletes,bg="lightcoral",fg="white",bd=4,padx=2,pady=2,font=("Helvetica",12,"bold"))
delete.grid(row=3,column=0)
all=tk.Button(root,text="Delete All Tasks", width=15, command=delete_all,bg="lightcoral",fg="white",bd=4,padx=2,pady=2,font=("Helvetica",12,"bold"))
all.grid(row=4,column=0)
ex=tk.Button(root,text="Exit", width=15, command=exit,bg="lightcoral",fg="white",bd=4,padx=2,pady=2,font=("Helvetica",12,"bold"))
ex.grid(row=5,column=0)
list=tk.Listbox(root,height=13,width=25,bg="lightcyan1",font=("Helvetica",12,"bold"))
list.grid(row=2,column=1,rowspan=4)

root.mainloop()