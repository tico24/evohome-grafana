from evohomeclient2 import EvohomeClient
from influxdb import InfluxDBClient
from requests.exceptions import ConnectionError
import time
import os
import requests

print("Starting")
username = os.environ['EH-USERNAME']
password = os.environ['EH-PASSWORD']

starttime = time.time()
if __name__ == "__main__":
    while True:
        # Connect to Influxdb
        try:
            client = InfluxDBClient(host='influxdb', port=8086)
            print("Connected to InfluxDB")
            client.create_database("EH-TEMPS")
            client.get_list_database()

            # Collect and store evohome temperatures
            eclient = EvohomeClient({username}, {password})
            for device in eclient.temperatures():
                print([{"measurement":"Temperatures","fields":device}])
                client.write_points([{"measurement":"Temperatures","fields":device}], database='EH-TEMPS')

            # Collect and store OH temperatures
            if "OW" in os.environ:
                API_key = os.environ['OW-API-KEY']
                city_name = os.environ['OW-CITY']
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                Final_url = base_url + "q=" + city_name + "&appid=" + API_key + "&units=metric"
                weather_data = requests.get(Final_url).json()
                temp = weather_data['main']['temp']
                print([{"measurement":"ext-Temperatures","fields":{'ext-temp': '%s' % temp}}])
                client.write_points([{"measurement":"ext-Temperatures","fields":{'ext-temp': '%s' % temp}}], database='EH-TEMPS')
        
        except ConnectionError as e:
            print("No Database Connection")
        time.sleep(600.0 - ((time.time() - starttime) % 600.0))