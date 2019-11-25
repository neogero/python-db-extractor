import jaydebeapi
import jpype

def db_connection(configuration):
    conn = jaydebeapi.connect(configuration['libName'], configuration['connectionUri'], [configuration['user'], configuration['password']], configuration['libUri'])
    
    return conn
    
def db_close(connection):
    connection.close()
    return 0
