import cx_Oracle

class PaymentException(Exception):
    pass

class Payment:
    def __init__(self, db):
        self.db = db

    def create(self, reservation_id:int, amount:float, payment_method:str):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("INSERT INTO Payment (reservation_id, amount, payment_method) "
                           "VALUES (:reservation_id, :amount, :payment_method)",
                           {
                               "reservation_id": reservation_id,
                               "amount": amount,
                               "payment_method": payment_method
                            })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise PaymentException(f'Payment database error: {error_obj.message}')
        except Exception as e:
            raise PaymentException(f'Payment error: {e}')

    def update(self, attribute:str, value, reservation_id:int):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(f"UPDATE Payment SET {attribute} = :value WHERE reservation_id = :reservation_id",
                           {
                               "value": value,
                               "reservation_id": reservation_id
                           })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise PaymentException(f'Payment database error: {error_obj.message}')
        except Exception as e:
            raise PaymentException(f'Payment error: {e}')

    def delete(self, reservation_id:int):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(f"DELETE FROM Payment WHERE reservation_id = :reservation_id",
                           {
                               "reservation_id": reservation_id
                           })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise PaymentException(f'Payment database error: {error_obj.message}')
        except Exception as e:
            raise PaymentException(f'Payment error: {e}')