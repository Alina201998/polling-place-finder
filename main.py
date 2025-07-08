# import pyodbc
# import tkinter as tk

# # 36105 24 73960 50
# # Connection String
# # Connection details
# conn = pyodbc.connect(
#     r'Driver=SQL Server;'
#     r'Server=Alina-zen;'
#     r'Database=master;'
#     r'Trusted_Connection=yes;'
#     )

# # to create a cursor
# crs = conn.cursor()
# # to create a cursor that returns list instead of default tuples
# # cursor = connection.cursor(dictionary=True)


# def polling_place():
#     try:
#         input_zip = int(txt1.get())
#         input_precinct = int(txt2.get())
#     except ValueError:
#         print("Invalid input. Please enter numeric values for zip code and precinct number.")
#         return


#     query = ("SELECT Polling_place_name, P.address "
#          "FROM Polling_place P "
#          "JOIN Voters V on P.polling_place_id = V.polling_place_id "
#          "WHERE V.zip_code = ? AND precinct_number = ?;")
#     #execute the query
#     crs.execute(query, (input_zip, input_precinct))

#     #to fetch data(returns Tuple!)
#     row= crs.fetchone()
#     if row:
#         result_label.config(text=f"Polling place: {row[0]}\n Address: {row[1]}") #row[0]: This accesses the first element in the tuple, which corresponds to the first column in your SELECT query (Polling_place_name in this case).
#     else:
#         result_label.config(text="No results found.")
    
    
    
    
    
# # Main application window
# root = tk.Tk()
# root.title("Choose or Lose")
# root.geometry("450x350")
# root.configure(bg='ivory2')

# # Title
# title_label = tk.Label(
#     root,
#     text="🗳️ Where Do I Vote?",
#     font=("Calibri", 24, "bold"),
#     bg="ivory2",
#     fg="#333"
    
# )


# # ZIP input
# lbl1 = tk.Label(root, text="Enter zip", font="Calibri 16", bg="ivory2")
# lbl1.pack()
# txt1 = tk.Entry(root, width=15)
# txt1.pack(pady=5)

# # Precinct number input
# lbl2 = tk.Label(root, text="Enter precinct", font="Calibri 16", bg="ivory2")
# lbl2.pack()
# txt2 = tk.Entry(root, width=15)
# txt2.pack(pady=5)

# # Button
# button = tk.Button(root, text="Click", font="Calibri 16", command=polling_place)
# button.pack(pady=10)

# # Program output
# result_label = tk.Label(root, text="", font="Calibri 16", bg="ivory2", wraplength=350)
# result_label.pack(pady=20)

# root.mainloop()
    
    
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
