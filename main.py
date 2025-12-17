# NOTE:
# This application uses a local SQL Server instance (Windows Trusted Connection).
# To run the app, the database schema and sample data must be created locally.
# See schema.sql and insert scripts included in this repository.
    
    
import pyodbc
import tkinter as tk

# Connect to database
conn = pyodbc.connect(
    r'Driver=SQL Server;'
    r'Server=Alina-zen;'
    r'Database=master;'
    r'Trusted_Connection=yes;'
)
crs = conn.cursor()

def polling_place():
    try:
        input_zip = int(txt_zip.get())
        input_precinct = int(txt_precinct.get())
    except ValueError:
        result_label.config(text="❌ Please enter valid ZIP and Precinct numbers.")
        return

    query = (
        "SELECT Polling_place_name, P.address "
        "FROM Polling_place P "
        "JOIN Voters V ON P.polling_place_id = V.polling_place_id "
        "WHERE V.zip_code = ? AND precinct_number = ?;"
    )
    crs.execute(query, (input_zip, input_precinct))
    row = crs.fetchone()

    if row:
        result_label.config(text=f"📍 Polling place: {row[0]}\n🏛️ Address: {row[1]}")
    else:
        result_label.config(text="No results found.")

# GUI
root = tk.Tk()
root.title("Choose or Lose")
root.geometry("450x350")
root.configure(bg='ivory2')

title_label = tk.Label(root, text="🗳️ Where Do I Vote?", font=("Calibri", 24, "bold"), bg="ivory2", fg="#333")
title_label.pack(pady=10)

# ZIP input
lbl_zip = tk.Label(root, text="Enter ZIP", font="Calibri 16", bg="ivory2")
lbl_zip.pack()
txt_zip = tk.Entry(root, width=15)
txt_zip.pack(pady=5)

# Precinct number input
lbl_precinct = tk.Label(root, text="Enter Precinct", font="Calibri 16", bg="ivory2")
lbl_precinct.pack()
txt_precinct = tk.Entry(root, width=15)
txt_precinct.pack(pady=5)

# Button
button = tk.Button(root, text="Search", font="Calibri 16", command=polling_place)
button.pack(pady=10)

# Output
result_label = tk.Label(root, text="", font="Calibri 14", bg="ivory2", wraplength=350, justify="left")
result_label.pack(pady=10)

root.mainloop()

