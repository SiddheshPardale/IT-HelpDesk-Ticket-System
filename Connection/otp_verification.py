import ConfigureDB as Db

Db.cursor1.execute("""
CREATE TABLE IF NOT EXISTS otp_verification (
    otp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    otp_hash TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expires_at TEXT NOT NULL,
    is_used INTEGER NOT NULL DEFAULT 0
        CHECK (is_used IN (0, 1)),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")
print("OTP Table Created....")


#-------------------------------------
#inserting the data 


user_id = int(input("Enter User ID: "))
otp_hash = input("Enter OTP Hash: ")
expires_at = input("Enter Expiry (YYYY-MM-DD HH:MM:SS): ")

Db.cursor1.execute("""
INSERT INTO otp_verification (user_id, otp_hash, expires_at)
VALUES (?, ?, ?)
""", (user_id, otp_hash, expires_at))

Db.conn.commit()
print("OTP Record Inserted!")