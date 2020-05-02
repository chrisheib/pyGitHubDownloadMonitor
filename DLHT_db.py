import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_tables(conn):
    # create tables
    if conn is not None:

        sql_create_files_table = """ CREATE TABLE IF NOT EXISTS files (
                                            name text NOT NULL,
                                            version text NOT NULL,
                                            UNIQUE(name,version)
                                        ); """

        sql_create_data_table = """ CREATE TABLE IF NOT EXISTS data (
                                            filesID integer NOT NULL,
                                            date text NOT NULL,
                                            count integer NOT NULL,
                                            UNIQUE(filesID,date)
                                        ); """

        create_table(conn, sql_create_files_table)
        create_table(conn, sql_create_data_table)
    else:
        print("Error! cannot create the database connection.")

def select(conn, sql, args=None):
    cur = conn.cursor()
    cur.execute(sql, args)
    return cur.fetchall()

def ReadValue(conn, table, field, where="1=1", args=None):
    row = select(conn, "SELECT " + field + " FROM " + table + " WHERE " + where + " LIMIT 1", args)[0]
    return row[0]

def exists(conn, sql, args=None):
    rows = select(conn,sql,args)
    return len(rows) > 0

def add_data(conn, date, filename, version, count):
    select(conn, "INSERT OR IGNORE INTO files (name, version) values (?,?)", [filename, version])
    filesID = ReadValue(conn, "files", "ROWID", "name = ? and version = ?", [filename, version])
    select(conn, "INSERT OR REPLACE INTO data (filesID, date, count) VALUES (?,?,?)", [filesID, date, count])