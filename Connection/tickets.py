import ConfigureDB as Db
Db.cursor1.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    ticket_id TEXT PRIMARY KEY,
    user_id INTEGER NOT NULL,
    category TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    priority TEXT NOT NULL
        CHECK (priority IN ('LOW','MEDIUM','HIGH','CRITICAL')),
    status TEXT NOT NULL DEFAULT 'OPEN'
        CHECK (status IN (
            'OPEN','ASSIGNED','IN_PROGRESS',
            'WAITING_FOR_USER','RESOLVED','CLOSED'
        )),
    assigned_to INTEGER,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    sla_deadline TEXT,
    resolved_at TEXT,
    closed_at TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (assigned_to) REFERENCES users(user_id)
)
""")
print("Tickets Table Created....")


