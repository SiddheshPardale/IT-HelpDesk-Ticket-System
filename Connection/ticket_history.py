import ConfigureDB as Db
Db.cursor1.execute("""
CREATE TABLE IF NOT EXISTS ticket_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id TEXT NOT NULL,
    changed_by INTEGER NOT NULL,
    old_status TEXT,
    new_status TEXT NOT NULL,
    changed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id),
    FOREIGN KEY (changed_by) REFERENCES users(user_id)
)
""")
print("History Table Created....")

#-------------------------------------
#inserting the data 

ticket_id = input("Enter Ticket ID: ")
changed_by = int(input("Enter User ID who changed status: "))
old_status = input("Enter Old Status (or leave blank): ").upper()
new_status = input("Enter New Status: ").upper()

Db.cursor1.execute("""
INSERT INTO ticket_history
(ticket_id, changed_by, old_status, new_status)
VALUES (?, ?, ?, ?)
""", (ticket_id, changed_by, old_status or None, new_status))

Db.conn.commit()
print("History Inserted!")