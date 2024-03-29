import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sqlite3
import DLHT_db as db
import DLHT_config as conf
from datetime import datetime

def CreateGraph(connection):
    fig = plt.figure(figsize=[15,6])
    ax = plt.subplot2grid((1, 3), (0, 0), colspan=2)

    dateformat = "%Y-%m-%d"

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
            data1.append(datetime.strptime(entry[0], dateformat))
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
    ax.set_facecolor('xkcd:grey')
    name, repo = conf.getRepoData()

    # Find total:
    result = connection.execute('SELECT * FROM (SELECT count, date FROM data LEFT JOIN files on filesID = files.ROWID WHERE version = "total" ORDER BY date DESC limit 2) ORDER BY date')
    total = 0
    lastTotal = 0
    for row in result:
        lastTotal = total
        total = row[0]
    deltaTotal = total - lastTotal
    deltastring = ""
    if (deltaTotal > 0):
        deltastring = " (+" + str(deltaTotal) + ")"

    ax.set_title(name+'/'+repo + ": " + str(total) + deltastring + " \n(" + datetime.now().strftime("%d.%m.%Y %H:%M") + ")")

    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., facecolor='xkcd:grey', edgecolor='black')

    ax.set_axisbelow(True)
    ax.yaxis.grid(color='gray', linestyle='dashed')
    ax.xaxis.grid(color='gray', linestyle='dashed')
    _, x2 = ax.get_xlim()
    if conf.CropToOneMonth():
        ax.set_xlim(max(0, x2-30), max(x2 - 2,2))

    ax.xaxis_date()
    fig.autofmt_xdate()

    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=15, horizontalalignment='right')
    fig.patch.set(facecolor = 'xkcd:grey')

    plt.savefig(conf.ExePath('data/foo.svg'), bbox_inches='tight')
    if conf.ShowPicture():
        plt.show()
