A docker-compose stack to collect temperature data from your Honeywell Evohome system and to present it on a graph.

- Collects current zone temperature and demanded temperature.
- Can collect external temperature through Open Weather Map
- Displays the data on a pre-built grafana graph


# Get started
Build the container:
`docker build -t evohome .`

modify the env vars in the docker-compose file for evohome to match your evohome login

Then start docker-compose:
`docker-compose up -d`

This creates the database and grafana, it tells grafana how to connect to the database and provisions a basic graph showing requested and actual temperatures for each room.

Once it looks like it's settled, go to localhost:3000
The default username/pass for grafana is admin/admin

There should be a 'Temperatures' dashboard and the Influxdb datasource should exist.

If you go to the explore menu, you should be able to search the database. This is a very basic query:
http://localhost:3000/explore?orgId=1&left=%5B%22now-5y%22,%22now%22,%22InfluxDB%22,%7B%22datasource%22:%22InfluxDB%22,%22policy%22:%22default%22,%22resultFormat%22:%22time_series%22,%22orderByTime%22:%22ASC%22,%22tags%22:%5B%5D,%22groupBy%22:%5B%7B%22type%22:%22time%22,%22params%22:%5B%22$__interval%22%5D%7D,%7B%22type%22:%22fill%22,%22params%22:%5B%22null%22%5D%7D%5D,%22select%22:%5B%5B%7B%22type%22:%22field%22,%22params%22:%5B%22value%22%5D%7D,%7B%22type%22:%22mean%22,%22params%22:%5B%5D%7D%5D%5D,%22query%22:%22SELECT%20*%20from%20%5C%22Temperatures%5C%22%22,%22rawQuery%22:true%7D%5D


The script requests a data update from Evohome once every 10 minutes. If you make this too frequent, you get rate-limited by Evohome.


# Optional external temperatures
If you want to record external temps, ensure you set the "OW" environment variable to "true"

Sign up at https://openweathermap.org/ for a free account. You'll find an API key (they also email it to you).
Set the API key and City environment variables. City values can be found here: https://bulk.openweathermap.org/sample/ (note that 'city' often means 'city,country')

Note that it may take OpenWeatherMap a few hours to activate your api key. If you don't get data immediately, don't be concerned.

# Optional Healthchecks.io integration
Create a new (free) account at healthchecks.io
Set the schedule period to 15 minutes. Set the grace time to 1 hour.
Add the http requests url to the environment variable "HEALTHCHECKS-IO"

The container should ping healthchecks.io after each successful run. If healthchecks.io doesn't receive a ping after 1 hour, you will get notified.

# "Features"
- If you norse your Evohome username/password up, the influx db won't get created and grafana will cry. It should fix itself once you remember your login.
- The dockerfile does a git clone of the master of watchforstock/evohome-client. This should not be considered a secure or sane way to do things.
- There is no security on the Influxdb database.
