from influxdb import InfluxDBClient
import Secret

#build class
class Rose():
    dbClient = InfluxDBClient(Secret.host,Secret.port,Secret.username,Secret.password,Secret.dbName, ssl=False, verify_ssl=False)
    dbClient.switch_database(Secret.dbName)
