import ConfigureDB as Db
Db.cursor1.execute("""
CREATE TABLE IF NOT EXISTS ticket_comments (
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    comment TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")
print("Comments Table Created....")


#-------------------------------------
#inserting the data 

# ticket_id = input("Enter Ticket ID: ")
# user_id = int(input("Enter User ID: "))
# comment = input("Enter Comment: ")

# Db.cursor1.execute("""
# INSERT INTO ticket_comments (ticket_id, user_id, comment)
# VALUES (?, ?, ?)
# """, (ticket_id, user_id, comment))

# Db.conn.commit()
# print("Comment Inserted!")