# 🗳️ Choose or Lose – Polling Place Finder

**Choose or Lose** is a beginner-friendly Python GUI application that helps voters find their designated polling place based on ZIP code and precinct number.  
It combines **Python**, **Tkinter**, and **SQL Server** to simulate a real-world data-driven app.

---

## Features

| Feature                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| GUI with Tkinter        | Clean and user-friendly interface for input and results                     |
| SQL Server connection   | Retrieves data securely from a local relational database                    |
| Input validation         | Handles incorrect input with GUI error messages                             |
| Realistic data          | Uses sample polling locations and voter records                             |
| Responsive display       | Results wrap cleanly on smaller window sizes for readability                 |

---

## Technologies Used

- **Python 3**
- **Tkinter** (GUI framework)
- **pyodbc** (Database connection)
- **SQL Server** (Database backend)

---

## How It Works

1. User enters a **ZIP code** and **precinct number** into the GUI.
2. The app connects to the database using `pyodbc`.
3. A SQL query checks the voter table and returns:
   - Polling Place Name  
   - Address  
4. The app displays this info in the window or an error if no match is found.

---

## Database Schema

```sql
CREATE TABLE Polling_place (
    polling_place_id INT PRIMARY KEY,
    polling_place_name VARCHAR(100),
    address VARCHAR(100),
    city VARCHAR(50),
    state CHAR(2),
    zip_code CHAR(5)
);

CREATE TABLE Voters (
    voter_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    address VARCHAR(100),
    city VARCHAR(50),
    state CHAR(2),
    zip_code CHAR(5),
    precinct_number INT,
    polling_place_id INT,
    FOREIGN KEY (polling_place_id) REFERENCES Polling_place(polling_place_id)
);
