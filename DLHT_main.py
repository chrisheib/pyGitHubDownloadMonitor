import DLHT_db as db
import DLHT_config as conf
import DLHT_api as api
from datetime import date, datetime

if __name__ == "__main__":

    conn = db.create_connection(r"pythonsqlite.db")
    db.create_tables(conn)
    response = api.getReleaseList()
    for release in response:
        print(release["name"])
        for asset in release["assets"]:
            print("   " + asset["name"] + "   " + str(asset["download_count"]))
            db.add_data(conn, datetime.today().strftime('%Y-%m-%d'), asset["name"], release["name"], asset["download_count"])

    conn.commit()