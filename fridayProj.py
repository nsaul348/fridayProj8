import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to submit feedback to the database
def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    feedback = entry_feedback.get("1.0", tk.END)
    
    conn = sqlite3.connect('customer_feedback.db')
    c = conn.cursor()
    c.execute("INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)", (name, email, feedback))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Feedback submitted!")
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_feedback.delete("1.0", tk.END)

# Function to retrieve and print feedback
def retrieve_feedback():
    password = input("Enter password: ")
    correct_password = "pass123" 
    if password == correct_password:
        conn = sqlite3.connect('customer_feedback.db')
        c = conn.cursor()
        c.execute("SELECT * FROM feedback")
        rows = c.fetchall()
        for row in rows:
            print(row)
        conn.close()
    else:
        print("Incorrect password.")

# Create or connect to SQLite database and create table if it doesn't exist
conn = sqlite3.connect('customer_feedback.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS feedback
             (name TEXT, email TEXT, feedback TEXT)''')
conn.commit()
conn.close()

# Create main window
root = tk.Tk()
root.title("Customer Feedback")

# Create input fields and labels
label_name = tk.Label(root, text="Name")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_email = tk.Label(root, text="Email")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

label_feedback = tk.Label(root, text="Feedback")
label_feedback.pack()
entry_feedback = tk.Text(root, height=5, width=30)
entry_feedback.pack()

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_feedback)
submit_button.pack()

# Create retrieve button
retrieve_button = tk.Button(root, text="Retrieve Data", command=retrieve_feedback)
retrieve_button.pack()

# Run the application
root.mainloop()
