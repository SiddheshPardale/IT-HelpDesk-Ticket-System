from Connection import ConfigureDB as Db


#-------------------------------------
#inserting the data 

def CreateTicket(user_id):
    ticket_id = input("Enter Ticket ID: ")
    category = input("Enter Category: ")
    title = input("Enter Title: ")
    description = input("Enter Description: ")
    priority = input("Enter Priority: ").upper()
    
    Db.cursor1.execute("""
    INSERT INTO tickets
    (ticket_id, user_id, category, title, description, priority)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (ticket_id, user_id, category, title, description, priority))
    
    Db.conn.commit()
    print("Ticket Inserted!")