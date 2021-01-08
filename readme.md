docker build -t evohome .

modify the env vars for evohome to match your evohome login

docker-compose up -d

goto localhost:3000

default username/pass is admin/admin

There should be a 'Temperatures' dashboard. It looks rubbish at the moment, but it should show data.