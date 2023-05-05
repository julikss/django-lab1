from mysql import connector
class MysqlDB:
    def __init__(self):
        self.conn = connector.connect(
            user = 'root',
            password = 'Passwd1!',
            host = 'localhost',
            database = 'decanatdb'
        )
        self.create_table()

    def create_table(self):
        cur = self.conn.cursor()
        query = '''
            CREATE TABLE IF NOT EXISTS db3 (
                student_id INTEGER PRIMARY KEY NOT NULL,
                course INTEGER NOT NULL,
                group_name TEXT NOT NULL,
                student TEXT NOT NULL
            )'''
        cur.execute(query)
        cur.close()
        print('CREATED TABLE')
         
    def select_all_records(self):
        cur = self.conn.cursor()
        query = 'SELECT * FROM db3'
        cur.execute(query)
        records = cur.fetchall()
        cur.close()
        return records

    def insert(self, record):
        cur = self.conn.cursor()
        query = 'INSERT INTO db3 (student_id, course, group_name, student) VALUES (?,?,?,?)'
        cur.execute(query, record)
        records = cur.fetchall()
        cur.close()
        return records
    
    def delete_records(self):
        cur = self.conn.cursor()
        query = 'DELETE FROM db3'
        cur.execute(query)
        cur.close()

mysqlDB = MysqlDB()
