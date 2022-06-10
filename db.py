import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS place (id INTEGER PRIMARY Key, place text, total text, date text, "
                         "checking text, savings text, deposits text, savings_deposits text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM place")
        rows = self.cur.fetchall()
        return rows

    def insert(self, place, total, date, checking, savings, deposits, savings_deposits):
        self.cur.execute("INSERT INTO place VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                         (place, total, date, checking, savings, deposits, savings_deposits))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM place WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, place, total, date, checking, savings, deposits, savings_deposits):
        self.cur.execute("UPDATE place SET place = ?, total = ?, date = ?, checking = ?, savings = ?, deposits = ?, "
                         "savings_deposits = ? WHERE id = ?", (place, total, date, checking, savings, deposits,
                                                               savings_deposits, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# db = Database('store.db')
