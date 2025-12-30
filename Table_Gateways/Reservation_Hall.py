import cx_Oracle

class ReservationHallException(Exception):
    pass

class ReservationHall:
    def __init__(self, db):
        self.db = db

    def create(self, reservation_id:int, hall_id:int):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("INSERT INTO Reservation_Hall (reservation_id, hall_id) "
                           "VALUES (:reservation_id, :hall_id)",
                           {
                               "reservation_id": reservation_id,
                               "hall_id": hall_id
                            })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise ReservationHallException(f'Reservation hall database error: {error_obj.message}')
        except Exception as e:
            raise ReservationHallException(f'Reservation hall error: {e}')

    def update(self, reservation_id:int, hall_id:int):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("UPDATE Reservation_Hall SET hall_id = :hall_id WHERE reservation_id = :reservation_id",
                           {
                               "reservation_id": reservation_id,
                               "hall_id": hall_id
                           })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            self.db.connection.rollback()
            raise ReservationHallException(f'Reservation hall database error: {error_obj.message}')
        except Exception as e:
            raise ReservationHallException(f'Reservation hall error: {e}')

    def delete(self, reservation_id:int):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(f"DELETE FROM Reservation_Hall WHERE reservation_id = :reservation_id",
                           {
                               "reservation_id": reservation_id
                           })
            self.db.connection.commit()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args