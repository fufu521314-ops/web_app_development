from .db import get_db_connection

class Lot:
    @staticmethod
    def create(number, content, explanation):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO lots (number, content, explanation) VALUES (?, ?, ?)",
            (number, content, explanation)
        )
        conn.commit()
        lot_id = cursor.lastrowid
        conn.close()
        return lot_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        lots = conn.execute("SELECT * FROM lots").fetchall()
        conn.close()
        return [dict(l) for l in lots]

    @staticmethod
    def get_by_id(lot_id):
        conn = get_db_connection()
        lot = conn.execute("SELECT * FROM lots WHERE id = ?", (lot_id,)).fetchone()
        conn.close()
        return dict(lot) if lot else None

    @staticmethod
    def update(lot_id, number=None, content=None, explanation=None):
        conn = get_db_connection()
        if number:
            conn.execute("UPDATE lots SET number = ? WHERE id = ?", (number, lot_id))
        if content:
            conn.execute("UPDATE lots SET content = ? WHERE id = ?", (content, lot_id))
        if explanation:
            conn.execute("UPDATE lots SET explanation = ? WHERE id = ?", (explanation, lot_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(lot_id):
        conn = get_db_connection()
        conn.execute("DELETE FROM lots WHERE id = ?", (lot_id,))
        conn.commit()
        conn.close()
