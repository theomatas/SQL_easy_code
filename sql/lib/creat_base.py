import sqlite3 

class BDD():
    def __init__(self):
        self.conn = sqlite3.connect('..//data//ma_base.db')
        self.cursor = self.conn.cursor()  
        self.table = []
    def request(self,data):
        try:
            msg = self.cursor.execute(data).fetchall()
            self.conn.commit()
        except Exception as e:
            msg = [e]
        return msg
  
        