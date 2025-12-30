import cx_Oracle

class ServiceException(Exception):
    pass

class Service:
    def __init__(self, db):
        self.db = db

    def create(self, name:str, price_per_hour:float, optional:bool=True):
        is_optional = 1 if optional else 0
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("INSERT INTO Service (name, price_per_hour, optional) VALUES (:name, :price_per_hour, :is_optional)",
                           {
                               "name": name,
                               "price_per_hour": price_per_hour,
                               "is_optional": is_optional
                           })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise ServiceException(f'Service database error: {error_obj.message}')
        except Exception as e:
            raise ServiceException(f'Service error: {e}')

    def update(self, attribute:str, value, name:str):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(f"UPDATE Service SET {attribute} = :value WHERE name = :name",
                           {
                               "value": value,
                               "name": name
                           })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise ServiceException(f'Service database error: {error_obj.message}')
        except Exception as e:
            raise ServiceException(f'Service error: {e}')

    def delete(self, name:str):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(f"DELETE FROM Service WHERE name = :name",
                           {
                               "name": name
                           })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise ServiceException(f'Service database error: {error_obj.message}')
        except Exception as e:
            raise ServiceException(f'Service error: {e}')