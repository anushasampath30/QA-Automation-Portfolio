import sqlite3
class Database:
    def __init__(self,db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
    def create_users_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users 
        (id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT,
        status TEXT NOT NULL
        )
        """)
        self.connection.commit()
    def insert_user(self, user_id, username, email, status):
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO users (id, username, email, status)
        VALUES (?, ?, ?, ?)""",(user_id, username, email, status))
        self.connection.commit()
    def get_user(self,username):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT id,username,email,status 
                        FROM users
                        where username = ?""",(username,) )
        row = cursor.fetchone()
        return row
    def get_user_status(self,status):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT id,username,email,status
                        FROM users
                        WHERE status=?""",(status,))
        rows = cursor.fetchall()
        return rows
    def update_user_status(self, username, new_status):
        cursor = self.connection.cursor()
        cursor.execute("""UPDATE users
                        SET status = ?
                        WHERE username = ?""",(new_status,username))
        self.connection.commit()

    
