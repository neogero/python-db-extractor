import json
import csv
import sqlite3

def write_json_result(filename, collection, conf, date_time):
    filename = "%s%s-%s" %(conf['outputDirectory'], date_time, filename)
    #filename should be .json
    with open(filename, 'w') as file:
        file.write(json.dumps(collection))

def write_csv_result(file, collection, conf, date_time):
    file = "%s%s-%s" %(conf['outputDirectory'], date_time, file)
    
    if len(collection) > 0:
        keys = collection[0].keys()
    
        with open(file, 'w', encoding='utf8', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys, delimiter='|')
            dict_writer.writeheader()
            dict_writer.writerows(collection)
    else:
        print('Error - collection is empty')

def writeSQLiteTable(name, collection, conf):
    if len(collection)>0:

        # Connection to DB
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        keys = collection[0].keys()


        # Creating Table
        dropTableSQL = "DROP table IF EXISTS " + name + ";"
        cur.execute(dropTableSQL)
        SQLCreateTable = generateSQLStringToCreateTableFromColumnsList(name, keys)
        print(SQLCreateTable)
        cur.execute(SQLCreateTable)

        # Inserting Data
        sql = generateSQLInsert(name, keys)
        print(sql)
        toDb=[]
        for element in collection:
            columns = element.values()
            values = []
            for column in columns:
                values.append(column)
            toDb.append(values)
            #cur.execute(sql, values)
        cur.executemany(sql, toDb)

        # Closing Connection
        con.commit()
        con.close()


    else:
        print('Error - collection is empty')


def generateSQLStringToCreateTableFromColumnsList(table, columns):
    createSQL = "CREATE TABLE " + table + " ("
    for column in columns:
        createSQL = createSQL + column + ", "
    createSQL = createSQL[:-2] + ");"
    return createSQL

def generateSQLInsert(table, columns):
    # creating INSERT SQL template
    sql = "INSERT INTO " + table + " ("

    for key in columns:
        sql = sql + key + ", "
    sql = sql[:-2] + ") VALUES ("

    for column in columns:
        sql = sql + "?, "
    sql = sql[:-2] + ");"

    return sql
