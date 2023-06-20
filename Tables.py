import sqlite3


def setup_db(connection: sqlite3.Connection) -> None:
    query = """
    CREATE TABLE IF NOT EXISTS exam_2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date STRING NOT NULL,
        math_analiz INTEGER,
        disk_math INTEGER,
        algebra INTEGER
    );
    """
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

    query = """
        CREATE TABLE IF NOT EXISTS hours_exam_2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            math_analiz INTEGER,
            disk_math INTEGER,
            algebra INTEGER
        );
        """
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
