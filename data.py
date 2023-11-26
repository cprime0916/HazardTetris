import sqlite3
class Data:
    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.cur = self.conn.cursor()
    def construct(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS data(
            id INT AUTO_INCREMENT PRIMARY KEY
            player_name TEXT
            score INT
        )""")
