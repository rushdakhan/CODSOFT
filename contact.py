import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
    clear_entries()
    messagebox.showinfo("Successful", "Contact added Successfully!")

def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")

def search_contact():
    search_term = search_entry.get()
    search_results.delete(0, tk.END)
    for contact in contacts:
        if search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]:
            search_results.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")

def update_contact():
    index = contact_list.curselection()
    if index:
        index = index[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        
        contacts[index] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        clear_entries()
        view_contacts()
        messagebox.showinfo("Successful", "Contact updated Successfully!")
    else:
        messagebox.showerror("Error", "Please select a contact to update!")

def delete_contact():
    index = contact_list.curselection()
    if index:
        index = index[0]
        del contacts[index]
        view_contacts()
        messagebox.showinfo("Successful", "Contact deleted Successfully!")
    else:
        messagebox.showerror("Error", "Please select a contact to delete!")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("670x550")
root.configure(background="darkseagreen1")

# Create UI elements
label1=tk.Label(root,text="Contact Book!",font=("Segoe Script", 28, "bold"),bg="darkseagreen1",fg="indigo")
label1.grid(row=0,column=0, columnspan=4)
name_label = tk.Label(root, text="Name:", font=("Georgia", 14, "bold"),bg="darkseagreen1")
name_label.grid(row=1, column=0, padx=10, pady=5)
name_entry = tk.Entry(root, width=25,bg="mistyrose1")
name_entry.grid(row=1, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="Phone:", font=("Georgia", 14, "bold"),bg="darkseagreen1")
phone_label.grid(row=2, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root, width=25,bg="mistyrose1")
phone_entry.grid(row=2, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:", font=("Georgia", 14, "bold"),bg="darkseagreen1")
email_label.grid(row=3, column=0, padx=10, pady=5)
email_entry = tk.Entry(root, width=25,bg="mistyrose1")
email_entry.grid(row=3, column=1, padx=10, pady=5)

address_label = tk.Label(root, text="Address:", font=("Georgia", 14, "bold"),bg="darkseagreen1")
address_label.grid(row=4, column=0, padx=10, pady=5)
address_entry = tk.Entry(root, width=25,bg="mistyrose1")
address_entry.grid(row=4, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Contact", command=add_contact, font=("Georgia", 14, "bold"), width=12,bg="darkslateblue",fg="white")
add_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

view_button = tk.Button(root, text="View Contacts", command=view_contacts, font=("Georgia", 14, "bold"), width=13,bg="darkslateblue",fg="white")
view_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

contact_list = tk.Listbox(root, width=40,bg="mistyrose1")
contact_list.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

update_button = tk.Button(root, text="Update Contact", command=update_contact, font=("Georgia", 14, "bold"),bg="darkslateblue",fg="white")
update_button.grid(row=7, column=2, padx=10, pady=5, sticky="we")

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, font=("Georgia", 14, "bold"),bg="darkslateblue",fg="white")
delete_button.grid(row=7, column=3, padx=10, pady=5, sticky="we")

search_label = tk.Label(root, text="Search:", font=("Georgia", 14, "bold"),bg="darkseagreen1")
search_label.grid(row=1, column=2, padx=10, pady=5)
search_entry = tk.Entry(root, width=25,bg="mistyrose1")
search_entry.grid(row=1, column=3, padx=10, pady=5)
search_button = tk.Button(root, text="Search", command=search_contact, font=("Georgia", 14, "bold"), width=10,bg="darkslateblue",fg="white")
search_button.grid(row=2, column=2, columnspan=2, padx=10, pady=5)

search_results = tk.Listbox(root, width=40,bg="mistyrose1")
search_results.grid(row=3, column=2, columnspan=2,rowspan=3, padx=10, pady=5)

root.mainloop()
