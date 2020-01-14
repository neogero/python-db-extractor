__author__ = "Gerardo Rodriguez"
__version__ = "1.0"
__status__ = "Develop"

import sys
import os
from datetime import datetime
import numpy as np

from src import configuration
from src import database
from src import files

def main():
    now = datetime.now()
    print(now)
    date_time = now.strftime("%Y%m%d-%H%M%S")
    print("\nJDBC DDBB Extractor v:%s\n" %(__version__))
    print("status: %s \n" %(__status__))
    print(date_time)

    conf = configuration.getConfiguration(sys.argv[1], os.getcwd())
    conn = database.db_connection(conf['connection'])

    for table in conf['tables']:
        result = export_table(conn, conf, table)
        result_file = table+'.csv'
        files.write_csv_result(result_file, result, conf, date_time)
        files.writeSQLiteTable(table, result, conf)

    database.db_close(conn)
    finish_time = datetime.now()
    print(finish_time)

def export_table(conn, conf, table):
    result_table=[]
    head=[]
    sql='SELECT * FROM ' + conf['database'] + '.' + table
    print(sql)

    cur = conn.cursor()
    cur.execute(sql)

    print('columns: ', len(cur.description))
    for description in cur.description:
        print(description[0])
        head.append(description[0])

    rows = cur.fetchall()
    for row in rows:
        regist = {}
        column_num = 0
        for column in head:
                regist[column] = row[column_num]
                column_num = column_num +1 

        result_table.append(regist)

    print('number of registers: ', len(result_table))
    cur.close()
    return result_table

if __name__ == "__main__":
    main()