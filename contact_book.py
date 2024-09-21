import tkinter as tk
from tkinter import messagebox

class Contact_Book:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = {}

        # Contact list frame
        self.contact_frame = tk.Frame(self.root)
        self.contact_frame.pack(pady=10)

        self.contact_listbox = tk.Listbox(self.contact_frame, width=50, height=10)
        self.contact_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.contact_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contact_listbox.yview)

        # Entry fields
        self.entry_name = tk.Entry(self.root, width=52)
        self.entry_name.pack(pady=10)
        self.entry_phone = tk.Entry(self.root, width=52)
        self.entry_phone.pack(pady=5)

        # Buttons
        self.add_contact_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_contact_button.pack(pady=5)

        self.remove_contact_button = tk.Button(self.root, text="Remove Contact", command=self.remove_contact)
        self.remove_contact_button.pack(pady=5)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        
        if name and phone:
            if name in self.contacts:
                messagebox.showwarning("Warning", "Contact already exists.")
            else:
                self.contacts[name] = phone
                self.update_contact_list()
                self.entry_name.delete(0, tk.END)
                self.entry_phone.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both name and phone number.")

    def remove_contact(self):
        try:
            selected_contact_index = self.contact_listbox.curselection()[0]
            selected_contact = self.contact_listbox.get(selected_contact_index).split(' - ')[0]
            del self.contacts[selected_contact]
            self.update_contact_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a contact to remove.")

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for name, phone in self.contacts.items():
            self.contact_listbox.insert(tk.END, f"{name} - {phone}")

if __name__ == "__main__":
    root = tk.Tk()
    contact_book_app = Contact_Book(root)
    root.mainloop()
