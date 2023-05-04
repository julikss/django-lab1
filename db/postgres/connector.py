import psycopg2

class PostgresDB:
    def __init__(self, path: str):
        self.conn = psycopg2.connect(path)
        self.create_table()
    
    def create_table(self):
        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS db2 (
                student_id INTEGER PRIMARY KEY NOT NULL,
                course INTEGER NOT NULL,
                group_name TEXT NOT NULL,
                student TEXT NOT NULL,
                subject TEXT NOT NULL
            )''')
        cur.close()
        print('CREATED TABLE')

    def read(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM db1")
        records = cur.fetchall()
        empty_table = records is None
        if empty_table:
            example = open('db/postgres/example.sql', 'r')
            script = example.read()

            self.conn.executescript(script)
            self.conn.commit()

        return records
    
    def create(self, data):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO db1 (student_id, course, group_name, student, subject) VALUES (%s, %s, %s, %s, %s)", data)
        cur.close()
        print("CREATED")

    def update(self, data):
        cur = self.conn.cursor()
        cur.execute("UPDATE db1 SET course = %s, group_name = %s, student = %s, subject = %s WHERE student_id = %s", 
                    (data[1], data[2], data[3], data[4], data[0]))
        cur.close()
        print("UPDATED")
    
    def delete(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM db1 WHERE student_id = %s", [id])
        cur.close()
        print("DELETED")
    
    def get_student(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM db1 WHERE student_id = %s", [id])
        student = cur.fetchall()
        cur.close()
        return student


postgresDB = PostgresDB("dbname=decanatdb user=postgres password=password")