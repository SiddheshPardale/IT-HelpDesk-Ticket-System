import ConfigureDB as Db

Db.cursor1.execute("""
CREATE TABLE IF NOT EXISTS ticket_attachments (
    attachment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id TEXT NOT NULL,
    uploaded_by INTEGER NOT NULL,
    filename TEXT NOT NULL,
    file_type TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    filedata BLOB NOT NULL,
    uploaded_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id),
    FOREIGN KEY (uploaded_by) REFERENCES users(user_id)
)
""")
print("Attachments Table Created....")

#-------------------------------------
#inserting the data 


ticket_id = input("Enter Ticket ID: ")
uploaded_by = int(input("Enter User ID: "))
path = input("Enter PDF/Image Path: ").strip().strip('"')

with open(path, "rb") as f:
    file_data = f.read()

filename = path.replace("\\", "/").split("/")[-1]

if filename.lower().endswith(".pdf"):
    file_type = "application/pdf"
elif filename.lower().endswith(".png"):
    file_type = "image/png"
elif filename.lower().endswith((".jpg", ".jpeg")):
    file_type = "image/jpeg"
else:
    raise ValueError("Only PDF, PNG, JPG and JPEG files are supported")

Db.cursor1.execute("""
INSERT INTO ticket_attachments
(ticket_id, uploaded_by, filename, file_type, file_size, filedata)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    ticket_id, uploaded_by, filename,
    file_type, len(file_data), file_data
))

Db.conn.commit()
print("Attachment Inserted!")
print("Attachment ID:", Db.cursor1.lastrowid)