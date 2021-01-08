Build the container:
`docker build -t evohome .`

modify the env vars in the docker-compose file for evohome to match your evohome login
Then start docker-compose
`docker-compose up -d`

This creates the database and grafana, it tells grafana how to connect to the database and provisions a basic graph (that almost certainly won't work unless you happen to have a room called 'Study')

Once it looks like it's settled, go to localhost:3000
The default username/pass for grafana is admin/admin

There should be a 'Temperatures' dashboard and the Influxdb datasource should exist.


If you go to the explore menu, you should be able to search the database. This is a very basic query:
http://localhost:3000/explore?orgId=1&left=%5B%22now-5y%22,%22now%22,%22InfluxDB%22,%7B%22datasource%22:%22InfluxDB%22,%22policy%22:%22default%22,%22resultFormat%22:%22time_series%22,%22orderByTime%22:%22ASC%22,%22tags%22:%5B%5D,%22groupBy%22:%5B%7B%22type%22:%22time%22,%22params%22:%5B%22$__interval%22%5D%7D,%7B%22type%22:%22fill%22,%22params%22:%5B%22null%22%5D%7D%5D,%22select%22:%5B%5B%7B%22type%22:%22field%22,%22params%22:%5B%22value%22%5D%7D,%7B%22type%22:%22mean%22,%22params%22:%5B%5D%7D%5D%5D,%22query%22:%22SELECT%20*%20from%20%5C%22Temperatures%5C%22%22,%22rawQuery%22:true%7D%5D


# "Features"
- If you norse your username/password up, the influx db won't get created and grafana will cry. It should fix itself once you remember you login.
- The dockerfile does a git clone of the master of watchforstock/evohome-client. This should not be considered a secure or sane way to do things.