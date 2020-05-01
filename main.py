import db
from datetime import date


if __name__ == "__main__":

    conn = db.create_connection(r"pythonsqlite.db")
    db.create_tables(conn)
    db.add_data(conn, date.today(), "nwo-donationmonitor-v0.8.0.zip", "v0.8.0", 500)
    row = db.select(conn, "SELECT name, version, count FROM files JOIN data on files.ROWID = data.filesID WHERE name = ? and date = ?", ["nwo-donationmonitor-v0.8.0.zip", date.today()])[0]
    print(row[0] + " " + row[1] + " " + str(row[2]))


