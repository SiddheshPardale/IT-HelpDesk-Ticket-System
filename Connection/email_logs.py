import ConfigureDB as Db

Db.cursor1.execute("""
CREATE TABLE IF NOT EXISTS email_logs (
    email_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    ticket_id TEXT,
    email_type TEXT NOT NULL,
    recipient TEXT NOT NULL,
    sent_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id)
)
""")
print("Email Logs Table Created....")

#-------------------------------------
#inserting the data 

user_id = int(input("Enter User ID: "))
ticket_id = input("Enter Ticket ID (or leave blank): ")
email_type = input("Enter Email Type: ")
recipient = input("Enter Recipient Email: ")
status = input("Enter Status (SENT/FAILED): ").upper()

Db.cursor1.execute("""
INSERT INTO email_logs
(user_id, ticket_id, email_type, recipient, status)
VALUES (?, ?, ?, ?, ?)
""", (
    user_id, ticket_id or None, email_type, recipient, status
))

Db.conn.commit()
print("Email Log Inserted!")
