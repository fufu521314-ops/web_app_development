from .db import get_db_connection

class Record:
    @staticmethod
    def create(user_id, lot_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO user_records (user_id, lot_id) VALUES (?, ?)",
            (user_id, lot_id)
        )
        conn.commit()
        record_id = cursor.lastrowid
        conn.close()
        return record_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        records = conn.execute(
            "SELECT user_records.*, lots.number, lots.content, lots.explanation "
            "FROM user_records JOIN lots ON user_records.lot_id = lots.id ORDER BY created_at DESC"
        ).fetchall()
        conn.close()
        return [dict(r) for r in records]

    @staticmethod
    def get_by_user_id(user_id):
        conn = get_db_connection()
        records = conn.execute(
            "SELECT user_records.*, lots.number, lots.content, lots.explanation "
            "FROM user_records JOIN lots ON user_records.lot_id = lots.id "
            "WHERE user_id = ? ORDER BY created_at DESC", 
            (user_id,)
        ).fetchall()
        conn.close()
        return [dict(r) for r in records]

    @staticmethod
    def get_by_id(record_id):
        conn = get_db_connection()
        record = conn.execute(
            "SELECT user_records.*, lots.number, lots.content, lots.explanation "
            "FROM user_records JOIN lots ON user_records.lot_id = lots.id WHERE user_records.id = ?",
            (record_id,)
        ).fetchone()
        conn.close()
        return dict(record) if record else None

    @staticmethod
    def update(record_id, lot_id):
        conn = get_db_connection()
        conn.execute("UPDATE user_records SET lot_id = ? WHERE id = ?", (lot_id, record_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(record_id):
        conn = get_db_connection()
        conn.execute("DELETE FROM user_records WHERE id = ?", (record_id,))
        conn.commit()
        conn.close()
