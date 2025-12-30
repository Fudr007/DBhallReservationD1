import cx_Oracle

class HallError(Exception):
    pass

class Hall:
    def __init__(self, db):
        self.db = db

    def create(self, name:str, sport_type:str, hourly_rate:float, capacity:int):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("INSERT INTO Hall (name, sport_type, hourly_rate, capacity) "
                           "VALUES (:name, :sport_type, :hourly_rate, :capacity)",
                           {
                               "name": name,
                               "sport_type": sport_type,
                               "hourly_rate": hourly_rate,
                               "capacity": capacity
                            })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise HallError(f'Hall database error: {error_obj.message}')

        except Exception as e:
            raise HallError(f'Hall error: {e}')


    def update(self, attribute:str, value, name):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(f"UPDATE Hall SET {attribute} = :value WHERE name = :name",
                           {
                               "value": value,
                               "name": name
                           })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise HallError(f'Hall database error: {error_obj.message}')
        except Exception as e:
            raise HallError(f'Hall error: {e}')

    def delete(self, name:str):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(f"DELETE FROM Hall WHERE name = :name",
                           {
                               "name": name
                           })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise HallError(f'Hall database error: {error_obj.message}')
        except Exception as e:
            raise HallError(f'Hall error: {e}')