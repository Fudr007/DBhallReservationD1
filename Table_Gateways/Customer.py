import cx_Oracle

class CustomerError(Exception):
    pass

class Customer:
    def __init__(self, db):
        self.db = db

    def create(self, name:str, email:str, phone:str, customer_type:str):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("INSERT INTO Customer (name, email, phone, customer_type) "
                           "VALUES (:name, :email, :phone, :customer_type)",
                           {
                               "name": name,
                                "email": email,
                                "phone": phone,
                                "customer_type": customer_type
                            })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise CustomerError(f'Customer database error: {error_obj.message}')

        except Exception as e:
            self.db.connection.rollback()
            raise CustomerError(f'Customer error: {e}')

    def update(self, attribute:str, value, email:str):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(f"UPDATE CUSTOMER SET {attribute} = :value WHERE email = :email",
                           {
                               "value": value,
                               "email": email
                           })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise CustomerError(f'Customer database error: {error_obj.message}')

        except Exception as e:
            self.db.connection.rollback()
            raise CustomerError(f'Customer error: {e}')

    def delete(self, email:str):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(f"DELETE FROM CUSTOMER WHERE EMAIL = :email",
                           {
                               "email": email
                            })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise CustomerError(f'Customer database error: {error_obj.message}')

        except Exception as e:
            self.db.connection.rollback()
            raise CustomerError(f'Customer error: {e}')

    def read(self, email:str):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM CUSTOMER WHERE email = :email",
                           {
                               'email': email
                           })
            return cursor.fetchone()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            raise CustomerError(f'Customer database error: {error_obj.message}')
        except Exception as e:
            raise CustomerError(f'Customer error: {e}')

    def read_all(self):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM CUSTOMER")
            return cursor.fetchall()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            raise CustomerError(f'Customer database error: {error_obj.message}')
        except Exception as e:
            raise CustomerError(f'Customer error: {e}')