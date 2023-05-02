import psycopg2

class PostgresDB:
    def __init__(self, path: str):
        self.conn = psycopg2.connect(path)
        #cur.execute("SELECT name FROM decanatdb WHERE type='table' AND name='decanat1'")
    
    def read(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM decanat1")
        records = cur.fetchall()
        return records
    
    def create(self, data):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO decanat1 (student_id, course, group_name, student, subject) VALUES (%s, %s, %s, %s, %s)", data)
        cur.close()
        print("CREATED")

    def update(self, data):
        cur = self.conn.cursor()
        cur.execute("UPDATE decanat1 course = %s, group = %s, student = %s, subject = %s WHERE id = %s", 
                    (data[1], data[2], data[3], data[4], data[0]))
        cur.commit()
        print("UPDATED")
    
    def delete(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM decanat1 WHERE id = %s", id)
        cur.commit()
        print("DELETED")

    def close(self):
        self.cur.close()

postgresDB = PostgresDB("dbname=decanatdb user=postgres password=password")