import sqlite3
class Data:
    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS leaderboard(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    player_name TEXT,
                    score INT
                )""")

    def push(self, name, score):
        sql = "INSERT INTO leaderboard (player_name, score) VALUES (?, ?)"
        val = (name, score)
        self.cur.execute(sql, val)
        self.conn.commit()
    def at(self, arg):
        if(arg.isnum()):
            sql = "SELECT player_name FROM leaderboard WHERE score = ?"
            val = (arg,)
            self.cur.execute(sql, val)
            self.conn.commit()
