# 🗳️ Choose or Lose – Polling Place Finder

**Choose or Lose** is a Python GUI application that helps voters find their designated polling place based on ZIP code and precinct number. It combines **Python**, **Tkinter**, and a **cloud-hosted Azure SQL Database** to simulate a real-world, data-driven application.

---

## Features

| Feature                  | Description                                                                 |
|---------------------------|-------------------------------------------------------------------------------|
| GUI with Tkinter           | Clean, modern interface for input and results                                 |
| Azure SQL Database         | Cloud-hosted relational backend — accessible from anywhere, not just one machine |
| Secure credential handling | Connection details stored in a git-ignored `.env` file, never hardcoded in source |
| Input validation            | Handles incorrect input with clear GUI error messages                          |
| Error handling               | Database connection failures are caught and shown as friendly messages, not raw crashes |
| Automated test suite         | 5 pytest tests validating query logic independently of the GUI                 |
| Realistic sample data         | Includes sample polling locations and voter records                           |

---

## Technologies Used

- **Python 3**
- **Tkinter / ttk** (GUI framework)
- **pyodbc** (Database connectivity)
- **Azure SQL Database** (cloud-hosted backend, T-SQL)
- **python-dotenv** (environment-based configuration)
- **pytest** (automated testing)

---

## How It Works

1. User enters a **ZIP code** and **precinct number** into the GUI.
2. The app connects to an **Azure SQL Database** using `pyodbc`, with credentials loaded securely from a local `.env` file.
3. A parameterized SQL query joins the `Voters` and `Polling_place` tables and returns:
   - Polling Place Name
   - Address
4. The app displays the result in the window, or a clear message if no match is found or an error occurs.

---

## Project Structure

```
├── main.py              # Application entry point — GUI + database logic
├── test_main.py         # Pytest suite for the query logic
├── schema.sql            # Table definitions (CREATE TABLE statements)
├── seed_data.sql         # Sample data (INSERT statements)
├── requirements.txt      # Python dependencies
├── .env                  # Local connection credentials (git-ignored, not included in repo)
└── .gitignore
```

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
```

---

## Cloud Migration: Local SQL Server → Azure SQL Database

This project originally ran against a local SQL Server instance. It has since been migrated to a fully cloud-hosted **Azure SQL Database** (free/serverless tier). Key changes made during the migration:

- **Connection authentication**: switched from Windows `Trusted_Connection` (only works when the app and database are on the same machine) to explicit SQL authentication (`Uid`/`Pwd`), required for any remote/cloud connection
- **Encryption**: added `Encrypt=yes` and `TrustServerCertificate=no` to the connection string, since data now travels over the public internet rather than staying local
- **Firewall configuration**: set up Azure firewall rules to allow only specific trusted IP addresses to connect to the database
- **Secrets management**: moved all connection details (server address, database name, username, password) into a `.env` file excluded from version control via `.gitignore` — nothing sensitive is hardcoded in `main.py`
- **Schema/data separation**: split the original combined SQL file into `schema.sql` (table definitions) and `seed_data.sql` (sample records), following standard project conventions

The T-SQL schema and query logic required **no changes** — Azure SQL Database uses the same SQL Server engine, so the migration was purely about connection configuration, security, and access management, not the underlying data logic.

---

## Testing

The core query logic is separated from the GUI (`get_polling_place()` in `main.py`) specifically to make it unit-testable. The test suite (`test_main.py`) covers:

- Known voters returning the correct polling place and address
- Non-existent ZIP codes returning no result (not an error)
- A valid ZIP paired with an incorrect precinct correctly returning no match (validates the query's filtering logic, not just its happy path)

Run the tests with:
```bash
pytest
```

---

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the project root with your own database credentials:
   ```
   DB_DRIVER=ODBC Driver 17 for SQL Server
   DB_SERVER=your-server.database.windows.net
   DB_DATABASE=your-database-name
   DB_USERNAME=your-username
   DB_PASSWORD=your-password
   ```
3. Run `schema.sql` then `seed_data.sql` against your database to create and populate the tables.
4. Run the app:
   ```bash
   python main.py
   ```
