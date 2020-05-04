import DLHT_db as db
import DLHT_config as conf
import DLHT_api as api
import DLHT_plot as plot
from datetime import date, datetime

if __name__ == "__main__":

    conn = db.create_connection(r"pythonsqlite.db")
    db.create_tables(conn)
    response = api.getReleaseList()
    totalCount = 0
    for release in response:
        print(release["name"])
        for asset in release["assets"]:
            print("   " + asset["name"] + "   " + str(asset["download_count"]))
            db.add_data(conn, datetime.today().strftime('%Y-%m-%d'), asset["name"], release["name"], asset["download_count"])
            totalCount += asset["download_count"]
    db.add_data(conn, datetime.today().strftime('%Y-%m-%d'), "total", "total", totalCount)

    conn.commit()
    plot.CreateGraph(conn)