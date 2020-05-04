import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import DLHT_db as db
import DLHT_config as conf

def CreateGraph(connection):
    plt.figure(figsize=[15,6])
    ax = plt.subplot2grid((1, 3), (0, 0), colspan=2)

    # Get Plotdata
    plotdata = []
    result = connection.execute('SELECT ROWID, version, name FROM files WHERE version <> "total" ORDER BY version DESC, name')
    for row in result:
        data = db.select(connection, 'SELECT date, count FROM data WHERE filesID = ? order by date', [row[0]])
        data1 = []
        data2 = []
        finalDL = 0
        lastDL = 0
        for entry in data:
            lastDL = finalDL
            data1.append(entry[0])
            data2.append(entry[1])
            finalDL = entry[1]

        dlDelta = finalDL - lastDL
        deltastring = ""
        if (dlDelta > 0):
            deltastring = " (+" + str(dlDelta) + ")"
        plotdata.append([data1,data2,row[1] + ' ' + row[2] + ': ' + str(finalDL) + deltastring])

    # Create new line for every file in the database
    for line in plotdata:
        ax.plot(line[0],line[1],label=line[2])

    ax.set_ylabel('Downloads')
    ax.set_xlabel('Date')
    name, repo = conf.getRepoData()

    # Find total:

    result = connection.execute('SELECT count FROM data LEFT JOIN files on filesID = files.ROWID WHERE version = "total" ORDER BY date DESC limit 2')
    total = 0
    lastTotal = 0
    for row in result:
        lastTotal = total
        total = row[0]
    deltaTotal = total - lastTotal
    deltastring = ""
    if (deltaTotal > 0):
        deltastring = " (+" + str(deltaTotal) + ")"

    ax.set_title(name+'/'+repo + ": " + str(total) + deltastring)

    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    ax.set_axisbelow(True)
    ax.yaxis.grid(color='gray', linestyle='dashed')
    ax.xaxis.grid(color='gray', linestyle='dashed')

    plt.savefig('foo.png', bbox_inches='tight')
    plt.show()