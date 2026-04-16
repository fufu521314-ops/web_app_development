from .db import get_db_connection

class Donation:
    @staticmethod
    def create(amount, message=None, user_id=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO donations (user_id, amount, message) VALUES (?, ?, ?)",
            (user_id, amount, message)
        )
        conn.commit()
        donation_id = cursor.lastrowid
        conn.close()
        return donation_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        donations = conn.execute("SELECT * FROM donations ORDER BY created_at DESC").fetchall()
        conn.close()
        return [dict(d) for d in donations]

    @staticmethod
    def get_by_id(donation_id):
        conn = get_db_connection()
        donation = conn.execute("SELECT * FROM donations WHERE id = ?", (donation_id,)).fetchone()
        conn.close()
        return dict(donation) if donation else None
        
    @staticmethod
    def get_by_user_id(user_id):
        conn = get_db_connection()
        donations = conn.execute("SELECT * FROM donations WHERE user_id = ? ORDER BY created_at DESC", (user_id,)).fetchall()
        conn.close()
        return [dict(d) for d in donations]

    @staticmethod
    def update(donation_id, amount=None, message=None):
        conn = get_db_connection()
        if amount is not None:
            conn.execute("UPDATE donations SET amount = ? WHERE id = ?", (amount, donation_id))
        if message is not None:
            conn.execute("UPDATE donations SET message = ? WHERE id = ?", (message, donation_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(donation_id):
        conn = get_db_connection()
        conn.execute("DELETE FROM donations WHERE id = ?", (donation_id,))
        conn.commit()
        conn.close()
