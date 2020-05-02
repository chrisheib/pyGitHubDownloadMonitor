import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import DLHT_db as db
import DLHT_config as conf

def CreateGraph(connection):
    fig = plt.figure(figsize=[15,6])
    #ax = fig.add_subplot(121)
    ax = plt.subplot2grid((1, 3), (0, 0), colspan=2)
    plotdata = []

    result = connection.execute('SELECT ROWID, version, name FROM files ORDER BY version DESC, name')
    for row in result:
        data = db.select(connection, 'SELECT date, count FROM data WHERE filesID = ? order by date', [row[0]])
        data1 = []
        data2 = []
        finalDL = 0
        for entry in data:
            data1.append(entry[0])
            data2.append(entry[1])
            finalDL = entry[1]
        plotdata.append([data1,data2,row[1] + ' ' + row[2] + ': ' + str(finalDL)])

    for line in plotdata:
        ax.plot(line[0],line[1],label=line[2])

    ax.set_ylabel('Downloads')
    ax.set_xlabel('Date')
    name, repo = conf.getRepoData()
    ax.set_title(name+'/'+repo)

    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    plt.savefig('foo.png', bbox_inches='tight')
    plt.show()