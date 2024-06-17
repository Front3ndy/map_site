import psycopg2 as ppg


class DBClient:
    """ Класс клиента для обращения к базе данных карты Архангельска
     Содержит метод соединения/разъединения с базой данных и методы запросов"""

    SELECT_TEMPLATE = """ SELECT * FROM map_app_category; """
    INSERT_TEMPLATE = """ INSERT INTO map_app_category ( id, category_name ) VALUES ( %s, %s ); """
    SELECT_OBJ_COORDS = """ SELECT obj_name, obj_coord, obj_address, image, obj_category_id FROM map_app_objectsdata; """

    def __init__(self, dbname, user, password, host):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host

    def connect(self):
        try:
            self.conn = ppg.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host)
        except:
            print('Не удалось подключиться к базе данных!')

    def get_coords(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.SELECT_OBJ_COORDS)
        data = self.cursor.fetchall()
        data_ed = []
        for i in data:
            data_ed.append({'name': i[0], 'coords': i[1], 'addr': i[2], 'img': i[3], 'category': i[4]})
        return data_ed

    def load_csv_with_copy(self):
        self.cursor = self.conn.cursor()

        # Use the COPY command to load the CSV file into the table
        with open('C:/Users/Vadim/PycharmProjects/site_for_hack/site_for_hack/data_utf.csv', "r", encoding='utf-8') as f:
            next(f)  # skip header row
            self.cursor.copy_from(f, 'map_app_objectsdata', sep=";")
            self.conn.commit()

        # Close the cursor and connection
        self.cursor.close()


    def select_execute(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.SELECT_TEMPLATE)
        return self.cursor.fetchall()

    def insert_execute(self):
        pass

    def shutdown(self):
        self.conn.close()


if __name__ == '__main__':
    db_client = DBClient('arh_map', 'map_user', 'mapper', 'localhost')
    db_client.connect()
    print(db_client.get_coords())
    db_client.shutdown()
