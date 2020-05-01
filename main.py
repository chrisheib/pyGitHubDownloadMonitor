import db


if __name__ == "__main__":

    conn = db.create_connection(r"pythonsqlite.db")
    db.create_tables(conn)

