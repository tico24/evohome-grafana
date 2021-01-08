from evohomeclient2 import EvohomeClient
from influxdb import InfluxDBClient
from requests.exceptions import ConnectionError
import time
import os

username = os.environ['EH-USERNAME']
password = os.environ['EH-PASSWORD']
eclient = EvohomeClient({username}, {password})

starttime = time.time()
if __name__ == "__main__":
    while True:
        # Connect to Influxdb
        try:
            client = InfluxDBClient(host='influxdb', port=8086)
            print("Connected to InfluxDB")
            client.create_database("EH-TEMPS")
            client.get_list_database()

            for device in eclient.temperatures():
                print([{"measurement":"Temperatures","fields":device}])
                client.write_points([{"measurement":"Temperatures","fields":device}], database='EH-TEMPS')
            
        except ConnectionError as e:
            print("No Database Connection")
        time.sleep(600.0 - ((time.time() - starttime) % 600.0))