from pathlib import Path
import sqlite3

BASE_DIR = Path(
    r"C:\Users\DELL\Desktop\LinkCode\Python\DBMS_Connectivity\IT-HelpDesk-System\Connection"
).resolve()
DATABASE_PATH = BASE_DIR / "helpdesk.db"

conn = sqlite3.connect(DATABASE_PATH)
cursor1 = conn.cursor()

conn.execute("PRAGMA foreign_keys = ON")

print("Database location:", DATABASE_PATH)